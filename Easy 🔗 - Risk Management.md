<h1>Risk Management</h1>


<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/c266a6d0-2717-4e5c-86f5-70c4ffb28c4c"></p>

<br>
<h2>Task 1 . Introduction</h2>
<p>You have just finished your work, prepared a hot cup of coffee, and decided to finish a new room on your favourite cyber security training platform. Now you want to enjoy your coffee while completing the room’s tasks; however, you pause momentarily and think, “What if the coffee spills on your desk and gets on your keyboard?” You can consider one of the following:<br>

- Enjoy your coffee before you finish a few more tasks. This way, you ensure that there is no way that coffee would get inside your keyboard.<br>
- Drink your coffee while doing new tasks. No matter how small, there is a chance that your coffee mug might spill and your keyboard would need to be serviced (or replaced).<br>
- You decide you cannot work without coffee, so you visit a nearby computer store and get yourself a keyboard protector or even a spill-resistant keyboard. This way, any coffee spill won’t cause any damage.<br>

Every activity entails some level of risk. In layperson’s terms, the risk is the possibility that something unwanted or harmful might happen due to an action or event. This thought process does not require any formal study of risk management. However, all three routes explored above can be valid responses to risks. In this case, it is the risk of spilling liquid on your keyboard.<br>

- If you decide not to bring coffee anywhere near your desk, that would be risk avoidance.<br>
- Drinking coffee while working with full knowledge of the risk would fall under risk acceptance.<br>
- Finally, upgrading your keyboard would be a risk reduction.<br>

Responses to risk will be explored and discussed in detail in a later section; however, we hope that this example from everyday life intrigues you to learn more about risk management formally.<br>

We will revisit this in more detail; however, risk management is a process of identifying, assessing, and responding to risks associated with a particular situation or activity. In Information Systems, risk management deals with threats to a computer system and its resources.</p>


<h3>Room Prerequisites</h3>
<p>This room has no strict prerequisites; however, studying it along with the Security Governance and Regulation and Threat Modelling rooms would be helpful.</p>


<h3>Learning Objectives</h3>
<p>By the end of this room, you will have learned about the following:<br>

- Vulnerability, Threat, and Risk<br>
- Information Systems Risk Management<br>
- Risk Management Process: Frame, Assess, Respond, and Monitor<br>
- Deciding how to respond to a risk</p>

<p><em>Answer the question below</em></p>

<p>1.1. <em>You have registered to attend a local workshop about offensive cyber security tools. The workshop requires the attendees to bring their own laptops. This workshop is critical for you, and you want to get the most out of it. Your laptop is good and reliable; however, as with any electronic device, there is always a chance, no matter how minuscule, that something might go wrong and it would fail.<br>You decide to carry an extra laptop; if your main laptop fails, the second laptop will be ready. What would you call this response to risk?</em><br>
<code>Risk Reduction</code></p>

<br>
<p>1.2. <em>You think your laptop has never failed before, and the chances of failing now are too slim. You decide not to take any extra actions. What do you call this response to risk?</em><br>
<code>Risk Acceptance</code></p>

<br>
<h2>Task 2 . Basic Terminology</h2>
<br>

<p><em>Answer the question below</em></p>


<br>
<p>2.1. <em>What do you call the potential for a loss or an incident that may harm the confidentiality, integrity or availability of an organisation’s information assets?</em><br>
<code>Risk</code></p>

<br>
<p>2.2. <em>What do you call a weakness an attacker could exploit to gain unauthorised access to a system or data?</em><br>
<code>Vulnerability</code></p>

<br>
<p>2.3. <em>What do you consider a business laptop?</em><br>
<code>Asset</code></p>

<br>
<p>2.4. <em>What do you consider a business laptop?</em><br>
<code>Threat</code></p>

<br>
<h2>Task 3 . Risk Assessment Methodologies</h2>
<p>There are several frameworks for risk assessment. Example methodologies are:<br>

- <strong>NIST SP 800-30</strong>: A risk assessment methodology developed by the National Institute of Standards and Technology (NIST). It involves identifying and evaluating risks, determining the likelihood and impact of each risk, and developing a risk response plan.<br>
- <strong>Facilitated Risk Analysis Process (FRAP)</strong>: A risk assessment methodology that involves a group of stakeholders working together to identify and evaluate risks. It is designed to be a more collaborative and inclusive approach to risk analysis.<br>
- <strong>Operationally Critical Threat, Asset, and Vulnerability Evaluation (OCTAVE)</strong>: A risk assessment methodology that focuses on identifying and prioritising assets based on their criticality to the organisation’s mission and assessing the threats and vulnerabilities that could impact those assets.<br>
- <strong>Failure Modes and Effect Analysis (FMEA)</strong>: A risk assessment methodology commonly used in engineering and manufacturing. It involves identifying potential failure modes for a system or process and then analysing the possible effects of those failures and the likelihood of their occurrence.>/p>


<h6 align="center"><img width="300px" src="https://github.com/user-attachments/assets/52304a13-5401-4b51-b1b9-b152ddba2135"><br>This image and all the theoretical content of<BR> the present article is TryHackMe´s property.</h6>

<p>Based on NIST SP 800-30, the risk management process entails four steps:<br>

- <strong>Frame risk</strong>: First, we must establish the context within which all risk activities occur.<br>
- <strong>Assess risk</strong>: We must identify, analyse, and evaluate potential risks and their likelihood and impact. This step is crucial to help decide on a proper response later.<br>
- <strong>Respond to risk</strong>: We need to take the steps necessary to mitigate the likelihood or impact of the risk. The response depends on many factors, and we will cover them separately.<br>
- <strong>Monitor risk</strong>: Finally, we continue tracking and evaluating the effectiveness of risk responses, identifying new risks, and ensuring that our risk management activities are effective. Monitoring is an ongoing process, as many criteria might change over time.<br>

We will discuss each in its own task.e Modes and Effect Analysis (FMEA): A risk assessment methodology commonly used in engineering and manufacturing. It involves identifying potential failure modes for a system or process and then analysing the possible effects of those failures and the likelihood of their occurrence.</p>

<br>
<p><em>Answer the question below</em></p>

<p>3.1. <em>What is the name of the risk assessment methodology developed by NIST?</em><br>
<code>NIST SP 800-30</code></p>

<br>
<h2>Task 4 . Frame Risk</h2>
<p>Risk management begins with establishing a risk context, i.e., framing risk. The purpose of risk framing is to develop a risk management strategy.</p>

<h6 align="center"><img width="300px" src="https://github.com/user-attachments/assets/945f4c65-e573-4b55-a229-0de7153d989d"><br>This image and all the theoretical content of<BR> the present article is TryHackMe´s property.</h6>

<p>Organisations must define a risk frame to set the groundwork for managing risk and provide limits to risk-based decisions. To create a reasonable risk frame, organisations must identify the following:<BR>

- <strong>Risk Assumptions</strong>: What are the assumptions about threats and vulnerabilities? What is the likelihood of occurrence? What would be the impact and consequences?<br>
- <strong>Risk Constraints</strong>: What are the constraints on assessing, responding, and monitoring risks?<br>
- <strong>Risk Tolerance</strong>: What are the acceptable levels of risk? What is the acceptable degree of risk uncertainty?<br>
- <strong>Priorities and Trade-offs</strong>: What are the high-priority business functions? What are the trade-offs among the different types of faced risks?</p>

<h3>Example Scenario</h3>
<p>Consider the case where you are part of the risk management team for an accounting company, and let’s revisit the above questions. We will avoid discussing risks and threats common to every company using information systems. In this example, we will only focus on one risk: data theft.<br>

- <strong>Risk Assumptionss</strong>: The fact that this company handles the accounting data of its clients increases the risk of being targeted by adversaries that would try to profit from stealing such data. Unless proper measures are taken, the likelihood of success is relatively high, and the impact would be disastrous for the company’s image.<br>
- <strong>Risk Constraintss</strong>: The primary constraints are expected to be budget-related. Safeguarding the data requires improving physical and cyber security; it entails conducting cyber security training and hiring new personnel.<br>
- <strong>Risk Tolerances</strong>: Considering the type of business, the risk of data theft cannot be tolerated. Tolerating data theft would lead to the whole company going out of business.<br>
- <strong>Priorities and Trade-offss</strong>: The priority is to maintain a trustworthy image of a company that can conduct its business with confidentiality and integrity.</p>

<p><em>Answer the question below</em></p>

<p>4.1. <em>Make sure you have read the above.</em><br>
<code>No answer needed</code></p>

<br>
<h2>Task 5 . Assess Risk</h2>

<br>
<p><em>Answer the question below</em></p>

<p>5.1. <em>Make sure you have read the above.</em><br>
<code>No answer needed</code></p>

<br>
<h2>Task 6 . Risk Analysis</h2>

<br>
<p><em>Answer the question below</em></p>

<p>6.1. <em>Ensure you have noted the mathematical formulas and the acronyms presented here, as they will be necessary to conduct quantitative risk analysis in later tasks.</em><br>
<code>No Answer needed</code></p>

<br>
<h2>Task 7 . Respond to Risk</h2>

<br>
<p><em>Answer the question below</em></p>

<p> 7.1. <em>Click on View Site. Decide whether each of the suggested safeguards (controls) is justified. Follow the instructions to retrieve the flag.</em><br>
<code>THM{Excellent_Risk_Management}</code></p>


<br>
<h2>Task 8 . Monitor Risk</h2>

<br>
<p><em>Answer the questions below</em></p>

<p>8.1. <em>You want to confirm whether the new policy enforcing laptop disk encryption is helping mitigate data breach risk. What is it that you are monitoring in this case?</em><br>
<code>Effectiveness</code></p>

<br>
<p>8.2. <em>You are keeping an eye on new regulations and laws. What is it that you are monitoring?</em><br>
<code>Compliance</code></p>


<br>
<h2>Task 9 . Supply Chain Risk Management</h2>

<br>
<p><em>Answer the question below</em></p>

<p>9.1. <em>Make sure that you have read the above.</em><br>
<code>No answer needed</code></p>

<br>
<h2>Task 10 . Putting It All Together</h2>

<br>
<p><em>Answer the question below</em></p>

<p>10.1. <em>Click on View Site and follow the instructions to retrieve the flag. Remember that your decision should be based on the value of the safeguard to the organisation, which is calculated as follows: ValueofSafeguard = ALEbeforeSafeguard − ALEafterSafeguard − AnnualCostSafeguard</em><br>
<code>THM{OFFICE_RISK_MANAGED}</code></p>






