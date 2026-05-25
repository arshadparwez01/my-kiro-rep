"""
Generate a PDF with 50 multiple-choice Ansible interview questions.

Usage:
    python generate_ansible_quiz.py

Produces:
    Ansible_Interview_Questions.pdf
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
)


QUESTIONS = [
    # ---------- BASICS ----------
    {
        "q": "Which statement best describes Ansible?",
        "options": [
            "A compiled programming language",
            "An agentless IT automation and configuration management tool",
            "A relational database engine",
            "A container runtime",
        ],
        "answer": "B",
        "explanation": (
            "Ansible is an open-source, agentless automation tool used for "
            "configuration management, application deployment, and orchestration."
        ),
    },
    {
        "q": "Which protocol does Ansible use by default to communicate with managed Linux nodes?",
        "options": ["FTP", "SSH", "Telnet", "SNMP"],
        "answer": "B",
        "explanation": (
            "Ansible connects to managed Linux/Unix nodes using SSH by default, "
            "which is why no agent is required on the target."
        ),
    },
    {
        "q": "Ansible is described as 'agentless'. What does that mean?",
        "options": [
            "It runs without any controller machine",
            "No persistent software needs to be installed on managed nodes",
            "It does not require Python",
            "It avoids using SSH keys",
        ],
        "answer": "B",
        "explanation": (
            "No long-running daemon is installed on the managed nodes; Ansible "
            "pushes modules over SSH (or WinRM) and executes them on demand."
        ),
    },
    {
        "q": "Which language are most Ansible modules written in?",
        "options": ["Ruby", "Go", "Python", "Bash"],
        "answer": "C",
        "explanation": (
            "Most core Ansible modules are written in Python, although modules "
            "can be written in any language that returns JSON."
        ),
    },
    {
        "q": "Which file format is primarily used to write Ansible playbooks?",
        "options": ["XML", "INI", "YAML", "TOML"],
        "answer": "C",
        "explanation": (
            "Ansible playbooks are written in YAML, which emphasizes human "
            "readability through indentation."
        ),
    },
    {
        "q": "What is the default location of the main Ansible configuration file?",
        "options": [
            "/etc/ansible/ansible.cfg",
            "/var/lib/ansible/config",
            "/usr/local/ansible.cfg",
            "/root/.ansible",
        ],
        "answer": "A",
        "explanation": (
            "The system-wide Ansible configuration file is /etc/ansible/ansible.cfg. "
            "It can be overridden by ANSIBLE_CONFIG, ./ansible.cfg, or ~/.ansible.cfg."
        ),
    },
    {
        "q": "Which component lists the hosts and groups that Ansible manages?",
        "options": ["Playbook", "Inventory", "Module", "Handler"],
        "answer": "B",
        "explanation": (
            "The inventory defines the hosts and groups that plays target. It "
            "can be static (INI/YAML) or dynamic (script/plugin)."
        ),
    },
    {
        "q": "Where is the default static inventory file located?",
        "options": [
            "/etc/ansible/hosts",
            "/etc/hosts",
            "/var/ansible/inventory",
            "/opt/ansible/hosts",
        ],
        "answer": "A",
        "explanation": (
            "By default Ansible reads /etc/ansible/hosts. You can override it "
            "with -i or with the inventory key in ansible.cfg."
        ),
    },
    {
        "q": "What does an Ansible 'play' represent?",
        "options": [
            "A single command run on a host",
            "A mapping of a group of hosts to a set of tasks",
            "A reusable unit of configuration like a role",
            "A connection plugin",
        ],
        "answer": "B",
        "explanation": (
            "A play maps hosts (or groups) to an ordered list of tasks to be "
            "executed against them."
        ),
    },
    {
        "q": "Which is the smallest unit of action in an Ansible playbook?",
        "options": ["Play", "Role", "Task", "Handler"],
        "answer": "C",
        "explanation": (
            "A task is a single call to an Ansible module and is the smallest "
            "executable unit inside a play."
        ),
    },

    # ---------- MODULES & TASKS ----------
    {
        "q": "Which Ansible module is used to manage packages on Red Hat-based systems?",
        "options": ["apt", "yum", "pacman", "zypper"],
        "answer": "B",
        "explanation": (
            "yum (or dnf) manages packages on RHEL/CentOS/Fedora. apt is for "
            "Debian/Ubuntu."
        ),
    },
    {
        "q": "Which module would you typically use to copy a file from the controller to a managed node?",
        "options": ["fetch", "copy", "synchronize", "template"],
        "answer": "B",
        "explanation": (
            "The copy module copies files from the control node to remote "
            "hosts. fetch goes the other direction."
        ),
    },
    {
        "q": "What is the primary difference between the copy and template modules?",
        "options": [
            "copy is faster than template",
            "template renders Jinja2 variables before copying; copy does not",
            "template only works on Windows hosts",
            "copy can only handle binary files",
        ],
        "answer": "B",
        "explanation": (
            "template processes the source file as a Jinja2 template, "
            "substituting variables, then transfers the rendered result."
        ),
    },
    {
        "q": "Which module is used to manage services (start/stop/enable)?",
        "options": ["service", "package", "command", "shell"],
        "answer": "A",
        "explanation": (
            "The service (or systemd) module manages service state and "
            "enable-on-boot behavior."
        ),
    },
    {
        "q": "Which module would you use to execute a shell command that requires shell features like pipes or redirection?",
        "options": ["command", "raw", "shell", "script"],
        "answer": "C",
        "explanation": (
            "The shell module runs commands through a shell, so it supports "
            "pipes, redirection, and shell variables. command does not."
        ),
    },
    {
        "q": "Which module runs a command WITHOUT going through a shell?",
        "options": ["shell", "command", "raw", "expect"],
        "answer": "B",
        "explanation": (
            "The command module executes the binary directly, so shell "
            "operators like |, <, > are treated as literal characters."
        ),
    },
    {
        "q": "Which Ansible concept makes most modules safe to run repeatedly with the same result?",
        "options": ["Concurrency", "Idempotency", "Reentrancy", "Parallelism"],
        "answer": "B",
        "explanation": (
            "Idempotency means a task only changes state when required, so "
            "repeated runs converge to the desired state without side effects."
        ),
    },
    {
        "q": "What does the 'changed' status of a task indicate?",
        "options": [
            "The task failed",
            "The module modified the target system to reach the desired state",
            "The task was skipped",
            "The task is deprecated",
        ],
        "answer": "B",
        "explanation": (
            "'changed' means the module took action because the system was "
            "not already in the desired state."
        ),
    },
    {
        "q": "Which module is best suited for editing single lines in an existing file?",
        "options": ["copy", "lineinfile", "template", "blockinfile"],
        "answer": "B",
        "explanation": (
            "lineinfile ensures a particular line exists (or is replaced) in "
            "a file. blockinfile manages multi-line blocks."
        ),
    },
    {
        "q": "Which module fetches files FROM remote hosts back to the controller?",
        "options": ["copy", "synchronize", "fetch", "get_url"],
        "answer": "C",
        "explanation": (
            "fetch retrieves files from managed hosts and stores them on the "
            "control node, typically organized per host."
        ),
    },

    # ---------- VARIABLES, FACTS, TEMPLATES ----------
    {
        "q": "Which Jinja2 syntax is used to reference a variable in a template?",
        "options": ["${var}", "{{ var }}", "<% var %>", "#{var}"],
        "answer": "B",
        "explanation": (
            "Jinja2 uses double curly braces for expressions: {{ variable }}."
        ),
    },
    {
        "q": "What are 'facts' in Ansible?",
        "options": [
            "User-defined variables in vars files",
            "Information automatically discovered about managed hosts",
            "Static playbook constants",
            "Encrypted secrets",
        ],
        "answer": "B",
        "explanation": (
            "Facts are data gathered from managed hosts (OS, IPs, memory, "
            "etc.) by the setup module at the start of a play."
        ),
    },
    {
        "q": "Which module gathers facts about managed hosts?",
        "options": ["gather", "facts", "setup", "info"],
        "answer": "C",
        "explanation": (
            "The setup module collects host facts. It is invoked automatically "
            "unless gather_facts: false is set."
        ),
    },
    {
        "q": "How do you disable automatic fact gathering for a play?",
        "options": [
            "facts: off",
            "gather_facts: false",
            "no_facts: true",
            "setup: skip",
        ],
        "answer": "B",
        "explanation": (
            "Set gather_facts: false at the play level to skip running the "
            "setup module."
        ),
    },
    {
        "q": "Which has the HIGHEST precedence among these variable sources?",
        "options": [
            "Role defaults",
            "Inventory group_vars",
            "Extra vars passed with -e",
            "Playbook vars",
        ],
        "answer": "C",
        "explanation": (
            "Extra variables (-e / --extra-vars) have the highest precedence "
            "in Ansible's variable precedence order."
        ),
    },
    {
        "q": "Which directive captures the output of a task into a variable?",
        "options": ["save", "register", "set_fact", "capture"],
        "answer": "B",
        "explanation": (
            "register stores the task's result in the named variable for use "
            "in subsequent tasks."
        ),
    },
    {
        "q": "Which module/directive sets a variable dynamically during a play?",
        "options": ["vars_prompt", "set_fact", "include_vars", "register"],
        "answer": "B",
        "explanation": (
            "set_fact creates new variables at runtime that persist for the "
            "remainder of the play (and can be made host-level facts)."
        ),
    },
    {
        "q": "Which Jinja2 filter provides a default value if a variable is undefined?",
        "options": ["fallback", "default", "or", "ifnull"],
        "answer": "B",
        "explanation": (
            "The default filter, e.g. {{ my_var | default('value') }}, is the "
            "idiomatic way to supply a fallback."
        ),
    },
    {
        "q": "Where should you place files that should be rendered by the template module in a role?",
        "options": [
            "files/",
            "templates/",
            "vars/",
            "tasks/",
        ],
        "answer": "B",
        "explanation": (
            "The template module looks in the role's templates/ directory "
            "for source files (typically *.j2)."
        ),
    },
    {
        "q": "Which directory in a role holds static files used by the copy module?",
        "options": ["files/", "templates/", "defaults/", "meta/"],
        "answer": "A",
        "explanation": (
            "The files/ directory in a role holds static content referenced "
            "by the copy and script modules."
        ),
    },

    # ---------- CONTROL FLOW ----------
    {
        "q": "Which keyword applies a condition to a task?",
        "options": ["if", "when", "only_if", "condition"],
        "answer": "B",
        "explanation": (
            "Use 'when:' followed by a Jinja2 expression to conditionally run "
            "a task."
        ),
    },
    {
        "q": "Which keyword iterates a task over a list of items?",
        "options": ["for", "loop", "each", "iterate"],
        "answer": "B",
        "explanation": (
            "loop: is the modern keyword for iteration; with_items is the "
            "older equivalent."
        ),
    },
    {
        "q": "What is a 'handler' in Ansible?",
        "options": [
            "A special task that runs only when notified by another task",
            "An alias for a role",
            "A connection plugin",
            "A type of inventory",
        ],
        "answer": "A",
        "explanation": (
            "Handlers are tasks invoked by 'notify'; they typically run once "
            "at the end of a play, e.g., to restart a service after a change."
        ),
    },
    {
        "q": "Which keyword is used to trigger a handler from a task?",
        "options": ["call", "trigger", "notify", "invoke"],
        "answer": "C",
        "explanation": (
            "A task uses 'notify: <handler name>' to schedule that handler "
            "for execution at the end of the play."
        ),
    },
    {
        "q": "Which keyword causes a play to keep running tasks even after a failure on a host?",
        "options": [
            "ignore_errors: true",
            "continue: true",
            "no_fail: true",
            "failed_when: false",
        ],
        "answer": "A",
        "explanation": (
            "ignore_errors: true makes Ansible record the failure but continue "
            "with subsequent tasks for that host."
        ),
    },
    {
        "q": "Which directive limits how many hosts run a play in parallel batches?",
        "options": ["forks", "serial", "throttle", "batch"],
        "answer": "B",
        "explanation": (
            "serial controls rolling-update batch size at the play level. "
            "forks is a global parallelism setting."
        ),
    },
    {
        "q": "Which keyword runs a task only once across all targeted hosts?",
        "options": ["once: true", "run_once: true", "delegate_to: localhost", "single: true"],
        "answer": "B",
        "explanation": (
            "run_once: true ensures the task executes on only one host "
            "(the first in the batch) regardless of how many are targeted."
        ),
    },
    {
        "q": "Which directive runs a task on a host different from the current target?",
        "options": ["delegate_to", "redirect_to", "run_on", "host_to"],
        "answer": "A",
        "explanation": (
            "delegate_to redirects task execution to a specified host while "
            "still being part of the current play."
        ),
    },
    {
        "q": "Which keyword tags tasks so they can be selectively run or skipped?",
        "options": ["labels", "tags", "marks", "scopes"],
        "answer": "B",
        "explanation": (
            "tags let you run subsets of a playbook with --tags or skip them "
            "with --skip-tags."
        ),
    },

    # ---------- ROLES, COLLECTIONS, GALAXY ----------
    {
        "q": "Which command initializes a new role skeleton?",
        "options": [
            "ansible-playbook init role",
            "ansible-galaxy init",
            "ansible-galaxy role init",
            "ansible role new",
        ],
        "answer": "C",
        "explanation": (
            "Modern syntax: ansible-galaxy role init <name>. The legacy "
            "shortcut 'ansible-galaxy init' also still works."
        ),
    },
    {
        "q": "Which directory in a role holds the default variables (lowest precedence)?",
        "options": ["vars/", "defaults/", "meta/", "vars_files/"],
        "answer": "B",
        "explanation": (
            "defaults/main.yml has the lowest precedence so consumers can "
            "easily override them; vars/ has higher precedence."
        ),
    },
    {
        "q": "Which file declares a role's dependencies on other roles?",
        "options": [
            "meta/main.yml",
            "tasks/main.yml",
            "defaults/main.yml",
            "handlers/main.yml",
        ],
        "answer": "A",
        "explanation": (
            "meta/main.yml lists dependencies, supported platforms, and "
            "Galaxy metadata for a role."
        ),
    },
    {
        "q": "What is an Ansible Collection?",
        "options": [
            "A bundle of related roles, modules, plugins, and playbooks distributed together",
            "A group of inventory hosts",
            "A snapshot of facts",
            "A type of vault file",
        ],
        "answer": "A",
        "explanation": (
            "Collections package and version content (modules, roles, "
            "plugins) and are distributed via Ansible Galaxy or a private hub."
        ),
    },
    {
        "q": "Which command installs a collection from Ansible Galaxy?",
        "options": [
            "ansible-galaxy install collection",
            "ansible-galaxy collection install",
            "ansible install-collection",
            "ansible-collection get",
        ],
        "answer": "B",
        "explanation": (
            "Use: ansible-galaxy collection install namespace.collection."
        ),
    },

    # ---------- VAULT, SECURITY, EXECUTION ----------
    {
        "q": "What is Ansible Vault used for?",
        "options": [
            "Storing inventory at scale",
            "Encrypting sensitive data such as passwords or keys in playbooks",
            "Caching facts between runs",
            "Logging task output securely",
        ],
        "answer": "B",
        "explanation": (
            "Ansible Vault encrypts variables and files so secrets can be "
            "safely committed to source control."
        ),
    },
    {
        "q": "Which command encrypts an existing plain-text file with Ansible Vault?",
        "options": [
            "ansible-vault encrypt <file>",
            "ansible vault lock <file>",
            "ansible-playbook --encrypt <file>",
            "ansible-galaxy encrypt <file>",
        ],
        "answer": "A",
        "explanation": (
            "ansible-vault encrypt <file> converts a plaintext file into an "
            "encrypted vault file."
        ),
    },
    {
        "q": "Which flag tells ansible-playbook to prompt for the vault password?",
        "options": ["--vault-prompt", "--ask-vault-pass", "--vault-password", "--secret"],
        "answer": "B",
        "explanation": (
            "Use --ask-vault-pass to be prompted interactively, or "
            "--vault-password-file for non-interactive runs."
        ),
    },
    {
        "q": "Which option simulates a playbook run without making changes?",
        "options": ["--dry-run", "--check", "--simulate", "--no-op"],
        "answer": "B",
        "explanation": (
            "--check enables Ansible's check mode (dry run). Use with --diff "
            "to also see file change previews."
        ),
    },
    {
        "q": "Which flag limits a playbook run to a subset of inventory hosts?",
        "options": ["--limit", "--hosts", "--filter", "--only"],
        "answer": "A",
        "explanation": (
            "--limit accepts a host pattern and restricts execution to "
            "matching hosts within the inventory."
        ),
    },
    {
        "q": "Which command-line tool is used to look up module documentation locally?",
        "options": ["ansible-help", "ansible-doc", "ansible-info", "ansible-man"],
        "answer": "B",
        "explanation": (
            "ansible-doc <module> shows documentation, parameters, and "
            "examples for the specified module/plugin."
        ),
    },
]


# ---------------------------------------------------------------------------
# PDF generation
# ---------------------------------------------------------------------------

def build_pdf(filename: str = "Ansible_Interview_Questions.pdf") -> None:
    assert len(QUESTIONS) == 50, f"Expected 50 questions, got {len(QUESTIONS)}"

    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
        title="Ansible Interview Questions",
        author="Interview Prep",
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        fontSize=22,
        leading=26,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#1F3A5F"),
        spaceAfter=12,
    )
    subtitle_style = ParagraphStyle(
        "SubtitleStyle",
        parent=styles["Normal"],
        fontSize=12,
        leading=16,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#444444"),
        spaceAfter=24,
    )
    section_style = ParagraphStyle(
        "SectionStyle",
        parent=styles["Heading2"],
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#1F3A5F"),
        spaceBefore=14,
        spaceAfter=8,
    )
    q_style = ParagraphStyle(
        "QStyle",
        parent=styles["Normal"],
        fontSize=11,
        leading=15,
        textColor=colors.black,
        spaceBefore=8,
        spaceAfter=4,
        alignment=TA_LEFT,
    )
    opt_style = ParagraphStyle(
        "OptStyle",
        parent=styles["Normal"],
        fontSize=10.5,
        leading=14,
        leftIndent=18,
        textColor=colors.HexColor("#222222"),
    )
    ans_style = ParagraphStyle(
        "AnsStyle",
        parent=styles["Normal"],
        fontSize=10.5,
        leading=14,
        leftIndent=18,
        textColor=colors.HexColor("#0B6E4F"),
        spaceBefore=4,
    )
    exp_style = ParagraphStyle(
        "ExpStyle",
        parent=styles["Normal"],
        fontSize=10,
        leading=13,
        leftIndent=18,
        textColor=colors.HexColor("#444444"),
        spaceAfter=10,
    )

    story = []

    # Cover
    story.append(Paragraph("Ansible Interview Questions", title_style))
    story.append(Paragraph(
        "50 multiple-choice questions covering the basics and core principles "
        "of Ansible, with answers and short explanations.",
        subtitle_style,
    ))

    sections = [
        (1, 10, "Section 1 - Ansible Basics & Architecture"),
        (11, 20, "Section 2 - Modules & Tasks"),
        (21, 30, "Section 3 - Variables, Facts & Templates"),
        (31, 40, "Section 4 - Control Flow, Handlers & Execution"),
        (41, 50, "Section 5 - Roles, Collections, Vault & Tooling"),
    ]

    current_section_idx = 0

    for idx, item in enumerate(QUESTIONS, start=1):
        # Section header
        if (current_section_idx < len(sections)
                and idx == sections[current_section_idx][0]):
            story.append(Paragraph(sections[current_section_idx][2], section_style))
            current_section_idx += 1

        flow = [Paragraph(f"<b>Q{idx}.</b> {item['q']}", q_style)]
        for letter, opt in zip("ABCD", item["options"]):
            flow.append(Paragraph(f"<b>{letter}.</b> {opt}", opt_style))
        flow.append(Paragraph(f"<b>Answer:</b> {item['answer']}", ans_style))
        flow.append(Paragraph(f"<i>Explanation:</i> {item['explanation']}", exp_style))

        # Keep each question with its options/answer together when possible
        story.append(KeepTogether(flow))

    doc.build(story)
    print(f"Wrote {filename}")


if __name__ == "__main__":
    build_pdf()
