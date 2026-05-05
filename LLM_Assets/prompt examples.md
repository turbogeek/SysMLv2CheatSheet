# Drone to kill Mosquitos

I want you to create an INCOSE discovery document, a requirements document, a logical SysMLv2 model, and a physical SysMLv2 model of a drone to kill mosquitos. The drone should be able to fly, hover, and shoot a laser to kill a mosquito. It should also have a camera and other sensors to detect mosquitos. Cover the whole lifecycle, from concept exploration through to disposal and recycling. Document your assumptions, measures of effectiveness, and measures of performance in the discovery document and derive the requirements from there in the SysML model. Include safety (there is a laser and the blades of the drone could be dangerous for humans) and security considerations, test cases, use cases, actors, stakeholders, stakeholder concerns, operational scenarios, operational needs, operational concepts, performance requirements, operating weather conditions, temperature ranges, reliability, maintenance, repairability, mission scenarios, trade studies, concept demonstrations, and a verification and validation plan. Read and apply the rules in `LLM_skills/skill.md`, follow the process in `LLM_skills/methodology_skill.md`, and use the template in `LLM_Assets/incose_template.md`. Also add some helpful tables and views in the model.

---

## 🛠️ Optional: Automated Validation Workflow (For Advanced Users)

If you have successfully installed the SysML v2 Java Validator and the `validate_model.py` script as outlined in the `Installation_Guide.md`, you can append the following instruction to **any** of the prompts above to enable self-correcting validation:

> **Validation Add-on:**
> "Please save the generated model to a file, and then use the `validate_model.py` script to validate the model. If the validator returns syntax errors, read `LLM_skills/fix_recipies.md` to learn how to fix the errors, and rewrite the model. Iterate automatically until the validator returns an exit code of 0."

## Train to deliver passengers

I want you to create an INCOSE discovery document and then a requirements document and then a logical SysMLv2 model and then a physical SysMLv2 model of a train to deliver passengers. The train should be able to operate autonomously on a track, accelerate, brake, and safely deliver passengers to their destinations. It should also have a camera and other sensors to detect obstacles on the tracks and maintain safe distances. Read and apply the rules in `LLM_skills/skill.md`, follow the process in `LLM_skills/methodology_skill.md`, and use the template in `LLM_Assets/incose_template.md`. Also add some helpful tables and views in the model.

## Automated Pool Maintenance Service Robot (Pool Maintenance Robot)

Create a model of an automated pool maintenance service robot. The robot should be able to calculate the amount of pool chlorine tablets needed to sanitize a pool. Use common knowledge about pool chemistry to create a model that is both accurate and easy to understand. The calculator should also include a feature that allows users to specify the type of chlorine they are using and the size of their pool. Understand the shape of common pools like play pool, kidney pool, and rectangular pool. Then model them as volumes and calculate the volume of the pool. Research the effect of temperature, rain, evaporation and other factors on the amount of chemicals needed to sanitize a pool. Then use this information to create a model that is both accurate and easy to understand. This tool will be used to create an automated pool maintenance service robot. Use the discovery doc to create an INCOSE compliant requirements document. Then create an INCOSE compliant logical SysMLv2 model and then an INCOSE compliant physical SysMLv2 model. Read and apply the rules in `LLM_skills/skill.md`, follow the process in `LLM_skills/methodology_skill.md`, and use the template in `LLM_Assets/incose_template.md`. Create any new data types, units, enumerations, and values as needed to fully model this system. Should have simple and complex analysis, for example: simple calculation of chlorine for a new pool, and complex calculation that includes rain, evaporation, and other factors related to the current amount of measured chemicals in the pool. Add tables, requirements, and viewpoints for safety, chemistry, logistics, maintenance of the robot, structure of the robot, ICD, requirements, reliability, cost, performance, trades and create corresponding views that use filters and expose of model elements to allow automated population of the tables and views in the model. Place the incose template result and the sysml model in "Prompt Examples Outputs/Pool_Maintenance_Robot_4_28_2026".

## Bicycle for personal transport

I want you to create an INCOSE discovery document and then a requirements document and then a logical SysMLv2 model and then a physical SysMLv2 model of a bicycle for personal transport. The bicycle should be able to operate on roads, accelerate, brake, and safely deliver passengers to their destinations. It should also have a camera and other sensors to detect obstacles on the road and maintain safe distances. Read and apply the rules in `LLM_skills/skill.md`, follow the process in `LLM_skills/methodology_skill.md`, and use the template in `LLM_Assets/incose_template.md`. Also add some helpful tables and views in the model.

## Simple Toaster

I want you to create an INCOSE discovery document and then a requirements document and then a logical SysMLv2 model and then a physical SysMLv2 model of a simple toaster. The toaster should be able to toast bread. Read and apply the rules in `LLM_skills/skill.md`, follow the process in `LLM_skills/methodology_skill.md`, and use the template in `LLM_Assets/incose_template.md`. Also add some helpful tables and views in the model.Use the MagicGrid process to create packages for Concept Exploration, Concept Definition, Logical Design, and Physical Design.

## Test prompt

Please create a simple requirements document, logical SysMLv2 model, and physical SysMLv2 model for a simple LED lightbulb. Follow the process in `LLM_skills/methodology_skill.md`, use the template in `LLM_Assets/incose_template.md`, and apply the rules in `LLM_skills/skill.md`. Don't worry about MagicGrid.
"Please save the generated model to a file, and then use the `validate_model.py` script to validate the model. If the validator returns syntax errors, read `LLM_skills/fix_recipies.md` to learn how to fix the errors, and rewrite the model. Iterate automatically until the validator returns an exit code of 0."

## Simple Alarm Clock

I want you to create an INCOSE discovery document and then a requirements document and then a logical SysMLv2 model and then a physical SysMLv2 model of a simple alarm clock. The alarm clock should be able to display the time, set an alarm, and sound an alarm when the alarm is set. Read and apply the rules in `LLM_skills/skill.md`, follow the process in `LLM_skills/methodology_skill.md`, and use the template in `LLM_Assets/incose_template.md`. Also add some helpful tables and views in the model. Use the MagicGrid process to create packages for Concept Exploration, Concept Definition, Logical Design, and Physical Design.

Please save the generated model to a file, and then use the `validate_model.py` script to validate the model. If the validator returns syntax errors, read `LLM_skills/fix_recipies.md` to learn how to fix the errors, and rewrite the model. Iterate automatically until the validator returns an exit code of 0.

## Simple Hobbyist Drone (Quick Start - Whole Process)

I want you to create an new instance of 'incose_template.md' for the following project: A simple hobbyist drone that should be able to record video, fly, hover, and land based on user input from a cell phone app. Use research about hobby drones to create stakeholders, stakeholder concerns, stakeholder needs, operational scenarios, operational needs, operational concepts, and stakeholder expectations, use cases and verifyable requirements. Features and capabilities should be on par with a $500 consumer price point. Use that information to create a SysMLv2 text file based on the information about SysMLv2 from 'skill.md' that follows the package structure of OOSEM or MagicGrid process with a concept, and logical,and physical SysMLv2 model. Also add some helpful views (table and views that use expose to automatically render data as diagrams or tables) in the model. Read and apply the rules in 'skill.md', follow the process in 'methodology_skill.md', and use the template in 'incose_template.md'.

If the user detects an error in the model and gives you feedback, document and correct the error, going back through the process as needed. Record changes and rational in a "corrections_iteration#.md" file, where '#' is the iteration number.

## Simple Hobbyist Ebike (Quick Start - Whole Process)

I want you to create an new instance of 'incose_template.md' for the following project: A simple hobbyist ebike that should be able to be ridden like a regular bike but also provide electric motor assist based on user input from a throttle, pedal assist sensor, and user selection of assist mode. The ebike should be able to operate on roads and trails, accelerate, brake, and safely assist the rider to their destination. It should also have a display to show speed, battery level, assist mode, and other relevant information. Features and capabilities should be on par with a $1500 consumer price point. Use research about hobby ebikes to create stakeholders, stakeholder concerns, stakeholder needs, operational scenarios, operational needs, operational concepts, and stakeholder expectations, use cases and verifyable requirements. Use that information to create a SysMLv2 text file based on the information about SysMLv2 from 'skill.md' that follows the package structure of OOSEM or MagicGrid process with a concept, and logical,and physical SysMLv2 model  Read and apply the rules in 'skill.md', follow the process in 'methodology_skill.md', and use the template in 'incose_template.md'. Also add some helpful views (table and views that use expose to automatically render data as diagrams or tables) in the model.

If the user detects an error in the model and gives you feedback, document and correct the error, going back through the process as needed. Record changes and rational in a "corrections_iteration#.md" file, where '#' is the iteration number.

---

## Enterprise Next-Gen Drone (Guided Milestones - Complex Project)

We are a commercial drone company building our next-generation drone designed for advanced applications such as crop inspection and neighborhood mosquito breeding ground search. I want you to act as our lead Systems Engineer and guide me through the INCOSE methodology using a **Guided Milestones** approach.

**Milestone 1: Concept Discovery**
Start by running the script `src/ntrs_api_client.py` using `LLM_skills/ntrs_skill.md` to search for "drone crop inspection" and "drone mosquito search" to gather technical constraints and state-of-the-art research. Then, use this data to fill out the Concept and System Goals sections of `LLM_Assets/incose_template.md`.
**PAUSE here and present the discovery documentation to me for review.**

**Milestone 2: Logical Architecture & Analysis**
Once I approve Milestone 1, move on to defining the Logical Architecture. You must include specific analysis goals for performance, safety, cost, and weight as guided by the objectives we established.
**PAUSE here and present the Logical Architecture and Analysis Goals to me for review.**

**Milestone 3: Physical Architecture & Tradeoff Studies**
Once I approve Milestone 2, move on to the Physical Architecture. Conduct tradeoff studies comparing at least two different physical implementations (e.g., battery vs hybrid power, fixed-wing vs quadcopter) using the analysis goals from Milestone 2. Document the tradeoff in `Doc` comments and justify your selected architecture.
**PAUSE here and present the final SysMLv2 model for validation using `validate_model.py`.**

Read and apply the rules in `LLM_skills/skill.md`, follow the iterative process in `LLM_skills/methodology_skill.md`, and use the template in `LLM_Assets/incose_template.md`.
