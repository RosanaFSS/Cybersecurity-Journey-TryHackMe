<h1 align="center">OWASP Top 10 2025: Application Design Flaws</h1>
<p align="center">2025, November 18  &nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure on my <code>1</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>Learn about A02, A03, A06, and A10 and how they related to design flaws in the application. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/owasptopten2025two">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/c69d3856-9874-4207-83cd-2f3af83627c3"></p>

<h2>Task 1 . Introduction</h2>
<h3>Set up your virtual environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting both your AttackBox (if you're not using your VPN) and Target Machines, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<p>This room breaks each 4 of the OWASP Top 10 2025 categories. In this room, you will learn about the categories that are related to failures in architecture and system design. You will put the theory into practice by completing supporting challenges. The following categories are covered in this room:<br>

- AS02: Security Misconfigurations<br>
- AS03: Software Supply Chain Failures<br>
- AS04: Cryptographic Failures<br>
- AS06: Insecure Design<br>

<h3>Deploy Practical</h3>
<p>Before we begin, please deploy the practical VM by clicking the green "Start Machine" button at the start of this task. Please note that you will need to use either the TryHackMe AttackBox or your own hacking machine connected to the TryHackMe VPN to access each practical.</p>

<p><em>Answer the question below</em></p>

<p>1.1. <em>I am ready to learn about IAAA failures!</em><br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 . AS02: Security Misconfigurations</h2>
<h3>Security Misconfigurations</h3>
<h4>What It Is</h4>
<p>Security misconfigurations happen when systems, servers, or applications are deployed with unsafe defaults, incomplete settings, or exposed services. These are not code bugs but mistakes in how the environment, software, or network is set up. They create easy entry points for attackers.</p>

<h4>Why It Matters</h4>
<p>Even small misconfigurations can expose sensitive data, enable privilege escalation, or give attackers a foothold into the system. Modern applications rely on complex stacks, cloud services, and third-party APIs. A single exposed admin panel, an open storage bucket, or misconfigured permissions can compromise the entire system.</p>

<h4>Example</h4>
<p>In 2017, <a href="https://www.huntress.com/threat-library/data-breach/uber-data-breach">Uber</a> exposed a backup AWS S3 bucket with sensitive user data, including driver and rider information, because the bucket was publicly accessible. Attackers could download data directly without needing credentials. This shows how a deployment mistake can lead to a significant breach.</p>

<h4>Common Patterns</h4>
<p>

- Default credentials or weak passwords left unchanged<br>
- Unnecessary services or endpoints exposed to the internet<br>
- Misconfigured cloud storage or permissions (S3, Azure Blob, GCP buckets)<br>
- Unrestricted API access or missing authentication/authorisation<br>
- Verbose error messages exposing stack traces or system details<br>
- Outdated software, frameworks, or containers with known vulnerabilities<br>
- Exposed AI/ML endpoints without proper access controls</p>

<h4>How To Prevent It</h4>
<p>

- Harden default configurations and remove unused features or services<br>
- Enforce strong authentication and least privilege across all systems<br>
- Limit network exposure and segment sensitive resources<br>
- Keep software, frameworks, and containers up to date with patches<br>
- Hide stack traces and system information from error messages<br>
- Audit cloud configurations and permissions regularly<br>
- Secure AI endpoints and automation services with proper access controls and monitoring<br>
- Integrate configuration reviews and automated security checks into your deployment pipeline</p>

<h3>Challenge</h3>
<p>Navigate to <code>MACHINE_IP:5002</code>. It appears that the developers left too many traces in their User Management APIs.</p>

<p><em>Answer the question below</em></p>

<p>2.1. <em>What's the flag?</em><br>
<code>THM{•••••••••••••••••}</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/a92581fa-eb20-490d-9cdd-deedd018d1bd"><br>
                   <img width="1200px" src="https://github.com/user-attachments/assets/25882d28-3efe-41c5-a676-ce6adf248b9d"></h6>


<br>
<h2>Task 3 . AS03: Software Supply Chain Failures</h2>
<h3>Software Supply Chain Failures</h3>
<h4>What It Is</h4>
<p>Software supply chain failures happen when applications rely on components, libraries, services, or models that are compromised, outdated, or improperly verified. These weaknesses are not inherent in your code, but rather in the software and tools you depend on. Attackers exploit these weak links to inject malicious code, bypass security, or steal sensitive data.</p>

<h4>Why It Matters</h4>
<p>Modern applications are built from many third-party packages, APIs, and AI models. One compromised dependency can compromise your entire system, allowing attackers to gain access without ever touching your own code. Supply chain attacks can be automated and distributed, making them hard to detect and very damaging.</p>

<h4>Example</h4>
<p>In 2021, the <a href="https://www.fortinet.com/uk/resources/cyberglossary/solarwinds-cyber-attack">SolarWinds</a> Orion compromise showed the danger of supply chain attacks. Attackers inserted malicious code into a trusted update, affecting thousands of organisations that automatically installed it. This wasn’t a bug in SolarWinds’ core logic. It was a flaw in the software update building, verification, and distribution process.<br>
With AI, we can observe this when using unverified third-party models or fine-tuned datasets that can embed hidden behaviours, backdoors, or biased outputs, compromising systems or leaking data.</p>

<h4>Common Patterns</h4>
<p>

- Using unverified or unmaintained libraries and dependencies<br>
- Automatically installing updates without verification<br>
- Over-reliance on third-party AI models without monitoring or auditing<br>
- Insecure build pipelines or CI/CD processes that allow tampering<br>
- Poor license or provenance tracking for components<br>
- Lack of monitoring for vulnerabilities in dependencies after deployment</p>

<h4>How To Prevent It</h4>
<p>

- Verify all third-party components, libraries, and AI models before use<br>
- Monitor and patch dependencies regularly<br>
- Sign, verify, and audit software updates and packages<br>
- Lock down CI/CD pipelines and build processes to prevent tampering<br>
- Track provenance and licensing for all dependencies<br>
- Implement runtime monitoring for unusual behaviour from dependencies or AI components<br>
- Integrate supply chain threat modelling into the SDLC, including testing, deployment, and update workflows

<h3>Challenge</h3>
<p>Navigate to <code>MACHINE_IP:5003</code>. The code is outdated and imports an old <code>lib/vulnerable_utils.py</code> component. Can you debug it?</p>

<p><em>Answer the question below</em></p>

<p>3.1. <em>What's the flag?</em> Hint: Check /api/process<br>
<code>THM{••••••••••••••••••••••••••••}</code></p>

<p>
  
- download <strong>Task File</strong><br>
- identify that the Python script checks <code>if data == 'debug':  return jsonify(debug_info())</code></p>

```bash
from flask import Flask, render_template, request, jsonify
import sys
import os

# Import from local unverified library
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))
from vulnerable_utils import process_data, format_output, debug_info

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/process', methods=['POST'])
def process():
    """Process user input using third-party library"""
    try:
        data = request.json.get('data', '')
        if not data:
            return jsonify({'error': 'Missing data parameter'}), 400
        
        # Check for debug mode 
        if data == 'debug':
            return jsonify(debug_info())
        
        processed = process_data(data)
        formatted = format_output(processed)
        
        return jsonify({
            'result': formatted,
            'status': 'success'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'version': '1.0.0'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

<p>

- navigate to the web application<br>
- identify that it processes and tranforms inputa data, accepting JSON payload with a data field containing the text to process in <code>/api/process</code><br>
- identify that it returns the current health status of the API service through <code>/api/health</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/4a9a176d-6b94-458a-86e2-c0d5b464ecaa"></h6>

<p>

- launch <strong>Burp Suite</strong><br>
- enable <strong>FoxyProxy</strong><br>
- navigate to <code>xx.xx.xxx.x:5003/api/process</code><br>
- right-click the intercepted request<br>
- select <code>Change request method</code><br>
- update <code>Content-Type</code> to <code>application/json</code>
- update <code>Content-Lenght</code> according to the json payload<br>
- eliminate the unnecessary headers<br>
- hit <code>Forward</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/c2d5cd3b-4903-4d85-8c52-a42a3078950a"></h6>

<br>
<h2>Task 4 . AS04: Cryptographic Failures</h2>
<h3>Cryptographic Failures</h3>
<h4>What It Is</h4>
<p>Cryptographic failures happen when encryption is used incorrectly or not at all. This includes weak algorithms, hard-coded keys, poor key handling, or unencrypted sensitive data. These flaws let attackers access information that should be private.</p>

<h4>Why It Matters</h4>
<p>Web applications rely on cryptography everywhere: protecting network traffic, securing stored data, verifying identities, and safeguarding secrets. When these controls fail, sensitive data such as passwords, tokens, or personal information can be exposed, leading to account takeovers or full-scale breaches.</p>

<h4>Example</h4>
<p>Attackers can exploit these flaws through man-in-the-middle attacks, brute-force attacks on weak keys, or by simply discovering secrets that were never properly protected.</p>

<h4>Common Patterns</h4>
<p>

- Using deprecated or weak algorithms like MD5, SHA-1, or ECB mode<br>
- Hard-coded secrets in code or configuration<br>
- Poor key rotation or management practices<br>
- Lack of encryption for sensitive data at rest or in transit<br>
- Self-signed or invalid TLS certificates<br>
- Using AI/ML systems without proper secret handling for model parameters or sensitive inputs</p>

<h4>How To Prevent It</h4>
<p>

- Use strong, modern algorithms such as AES-GCM, ChaCha20-Poly1305, or enforce TLS 1.3 with valid certificates<br>
- Use secure key management services like Azure Key Vault, AWS KMS, or HashiCorp Vault<br>
- Rotate secrets and keys regularly, following defined crypto periods<br>
- Document and enforce policies and standard operating procedures for key lifecycle management<br>
- Maintain a complete inventory of certificates, keys, and their owners<br>
- Ensure AI models and automation agents never expose unencrypted secrets or sensitive data<br>
- The web application in this room contains a weakness of this type for you to explore.</p>

<h3>Challenge</h3>
<p>Navigate to <code>MACHINE_IP:5004</code>. Can you find the key to decrypt the file?</p>

<p><em>Answer the question below</em></p>

<p>4.1. <em>What's the flag?</em><br>
<code>THM{••••••••••••••••••••••••••}</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/24ab0c57-b085-4d7e-aba1-8d0a32c2ceb4"></h6>

<p>

- view source page<br>
- identify <code>/static/js/decrypt.js</code><br>
- navigated to the path just discovered<br>
- identify <code>Base64</code> encoding in the <code>isValidDocumentFormat</code> function<br>
- identify <code>SECRET_KEY</code> : my-secret-key-16, <code>ENCRYPTION_MODE</code> : ECB</p>

<p><em>decrypt.js</em></p>

```bash
// Document encryption utilities
// Last updated: 2024-03-15

(function() {
    'use strict';
    
    // Configuration
    const SECRET_KEY = "my-secret-key-16";
    const ENCRYPTION_MODE = "ECB";
    const KEY_SIZE = 128;
    
    // Utility functions
    function formatTimestamp(date) {
        return date.toISOString().replace('T', ' ').substring(0, 19);
    }
    
    function validateDocumentId(id) {
        return /^[a-zA-Z0-9-_]+$/.test(id);
    }
    
    function getDocumentMetadata() {
        return {
            version: "1.2.3",
            encryptionEnabled: false,
            lastModified: formatTimestamp(new Date())
        };
    }
    
    // Logging utility
    function logEvent(eventType, details) {
        if (typeof console !== 'undefined' && console.log) {
            console.log(`[${formatTimestamp(new Date())}] ${eventType}:`, details);
        }
    }
    
    // Document validation
    function isValidDocumentFormat(data) {
        try {
            const decoded = atob(data);
            return decoded.length > 0 && decoded.length % 16 === 0;
        } catch (e) {
            return false;
        }
    }
    
    // Export to global scope if needed
    if (typeof window !== 'undefined') {
        window.documentUtils = {
            getMetadata: getDocumentMetadata,
            validateFormat: isValidDocumentFormat,
            validateId: validateDocumentId
        };
    }
    
    logEvent('INIT', 'Document utilities loaded');
})();
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/b8d9edad-ec93-4cf6-b1b8-fcee2286905c"></h6>

<br>
<h2>Task 5 . AS06: Insecure Design</h2>
<h3>Insecure Design</h3>
<h4>What It Is</h4>
<p>Insecure design happens when flawed logic or architecture is built into a system from the start. These flaws stem from skipped threat modelling, no design requirements or reviews, or accidental errors.<br>

Moreover, with the introduction of AI assistants, AI systems exacerbate insecure design. Developers often assume that models are safe, correct, or predictable, or that the code they produce is flaw-free. When an AI system can generate queries, write code, or classify users without limits, the risk is built into the design, leading to poor architectural patterns.</p>

<h4>Example</h4>
<p>A good example is <a href="https://www.fortinet.com/uk/resources/cyberglossary/solarwinds-cyber-attack">ClubHouse</a>. Its early design assumed users would only interact through the mobile app, but the backend API had no proper authentication. Anyone could query user data, room info, and even private conversations directly. When researchers tested it, "he entire "private c "nversation" premise fell apart.</p>

<h4>Why It Matters</h4>
<p>You can't patch an insecure design. It's built into the workflow, logic, and trust boundaries. Fixing it means rethinking how systems, and now AI, make decisions.</p>

<h4>Common Insecure Designs In 2025</h4>
<p>
  
- Weak business logic controls, like recovery or approval flows<br>
- Flawed assumptions about user or model behaviour<br>
- AI components with unchecked authority or access<br>
- Missing guardrails for LLMs and automation agents<br>
- Test or debug bypasses left in production<br>
- No consistent abuse-case review or AI threat modelling</p>

<h4>Insecure Design In The AI Era</h4>
<p>AI introduces new kinds of design failures. For example, prompt injection occurs when user input is blended with system prompts, allowing attackers to hijack the context or extract hidden data. Blind trust in model output creates fragile systems that act on AI decisions without validation or oversight, which is why human review remains necessary. When it comes to poisoned models, pulled from unverified sources or fine-tuned on unsafe data, they can embed hidden behaviours or backdoors that compromise the system from within.</p>

<h4>How To Design Securely</h4>
<p>

- Treat every model as untrusted until proven otherwise.<br>
- Validate and filter all model inputs and outputs to ensure accuracy and integrity.<br>
- Separate system prompts from user content.<br>
- Keep sensitive data out of prompts unless absolutely needed and protect it with strict controls.<br>
- Require human review for high-risk AI actions.<br>
- Log model provenance, monitor behaviour, and apply differential privacy for sensitive data.<br>
- Include AI-specific threat modelling for prompt attacks, inference risks, agent misuse, and supply chain compromise throughout the design process.<br>
- Build threat modelling into every stage of development, not just at the start.<br>
- Define clear security requirements for each feature before implementation.<br>
- Apply the principle of least privilege across users, APIs, and services.<br>
- Ensure proper authentication, authorisation, and session management across the system.<br>
- Keep dependencies, third-party components, and supply chain sources verified and up to date.<br>
- Continuously monitor and test the system for logic flaws, abuse paths, and emergent risks as new features or AI components are added.</p>

<h3>Challenge</h3>
<p>Navigate to <code>MACHINE_IP:5005</code>code>. Have they assumed that only mobile devices can access it?</p>

<p><em>Answer the question below</em></p>

<p>5.1. <em>What's the flag?</em><br>
<code>THM{••••••••••••••••••••••••••}</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/84e12209-340d-4f24-8d6d-ea0459415412"></h6>

<br>

```bash
:~/ApplicationDesignFlaws# gobuster dir -u http://xx.xx.xxx.x:5005/api/messages/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -q
/admin                (Status: 200) [Size: 154]
/user1                (Status: 200) [Size: 238]
/user2                (Status: 200) [Size: 114]
```

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/ad5a7f81-5a59-439a-92af-84c7d3a654aa"></h6>

<br>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/c13a6749-ff63-4c06-ad80-26d023d2ed70"></h6>

<br>
<h2>Task 6 . Conclusion</h2>
<h3>Conclusion</h3>
<p>Security design failures across AS02 Security Misconfigurations, AS03 Software Supply Chain Failures, AS04 Cryptographic Failures, and AS06 Insecure Design all come from the same root cause: weak foundations. You cannot add security at the end and expect it to work. Strong systems start with clear security requirements, realistic threat assumptions, controlled configurations, vetted dependencies, and sound cryptographic choices.<br>

Treat defaults with suspicion, treat every dependency as a potential risk, and keep design simple enough to reason about. Get the design right early, and you avoid a long future of preventable incidents.<br>

Continue the journey with Room 3 in this module: Application Design Flaws: <a href="https://tryhackme.com/jr/owasptop102025insecuredatahandling">https://tryhackme.com/jr/owasptop102025insecuredatahandling</a></p>

<p><em>Answer the question below</em></p>

<p>6.1. <em>I'm ready for the next room!</em><br>
<code>No answer needed</code></p>

<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/a4c6d528-4bf0-4a9f-b55b-0cd345f20b13"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/0b718b96-bfd9-4b78-80ea-ea6d5ba60d63"></p>


<h1 align="center">My TryHackMe Journey ・ 2025, November</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|18      |Easy 🔗 - OWASP Top 10 2025: Application Design Failures| 1   |      93ʳᵈ    |     3ʳᵈ    |     927ᵗʰ   |      8ᵗʰ     |    132,183  |    1,023    |    80     |
|18      |Easy 🔗 - OWASP Top 10 2025: IAAA Failures| 1   |      93ʳᵈ    |     3ʳᵈ    |     971ˢᵗ   |      8ᵗʰ     |    132,151  |    1,022    |    80     |
|14      |Hard 🚩 - Shock and Silence            |   1    |      94ᵗʰ    |     4ᵗʰ    |     749ᵗʰ   |      7ᵗʰ     |    133,095  |    1,021    |    80     |
|14      |Easy 🔗 - Input Manipulation & Prompt Injection| 1 |   95ᵗʰ    |     4ᵗʰ    |   1,290ᵗʰ   |     12ⁿᵈ     |    132,822  |    1,020    |    80     |
|14      |Hard 🚩 - CRM Snatch                   |   1    |      95ᵗʰ    |     4ᵗʰ    |   1,526ᵗʰ   |     12ⁿᵈ     |          -  |    1,019    |    80     |
|8       |Easy 🔗 - Living of the Land Attacks   |   1    |      91ˢᵗ    |     4ᵗʰ    |   1,759ᵗʰ   |     17ᵗʰ     |    132,642  |    1,018    |    80     |
|8       |Hard 🚩 - Lost in RAMslation           |   1    |      91ˢᵗ    |     4ᵗʰ    |   2,547ᵗʰ   |     25ᵗʰ     |    132,580  |    1,017    |    80     |
|8       |Easy 🔗 - MITRE                        |   1    |       -      |     4ᵗʰ    |      -      |      -       |          -  |       -     |    80     |

</h6></div><br>

<p align="center">Global All Time:     93ʳᵈ<br><img width="250px" src="https://github.com/user-attachments/assets/f3b63c7c-df0c-464f-be7c-ad18422cea87"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/829d7ed7-b628-49ce-8ae0-5224f8b3aef8"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/3e8f4f17-7be2-41f5-8e81-1ef2f74479f3"><br><br>
                  Global monthly:     927ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/308fb5c6-5ef7-4f98-9e42-13b8b08e3d46"><br><br>
                  Brazil monthly:       8ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/2aa5d004-d979-4e49-9860-e5c46d32f0cf"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>

