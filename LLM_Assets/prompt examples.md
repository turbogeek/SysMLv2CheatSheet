# Drone to kill Mosquitos

I want you to create an INCOSE discovery document, a requirements document, a logical SysMLv2 model, and a physical SysMLv2 model of a drone to kill mosquitos. The drone should be able to fly, hover, and shoot a dart to kill a mosquito. It should also have a camera and other sensors to detect mosquitos. Cover the whole lifecycle, from concept exploration through to disposal and recycling. Document your assumptions, measures of effectiveness, and measures of performance in the discovery document and derive the requirements from there in the SysML model. Include safety and security considerations, test cases, use cases, actors, stakeholders, stakeholder concerns, operational scenarios, operational needs, operational concepts, performance requirements, operating weather conditions, temperature ranges, reliability, maintenance, repairability, mission scenarios, trade studies, concept demonstrations, and a verification and validation plan. Read and apply the rules in `LLM_skills/skill.md`, follow the process in `LLM_skills/methodology_skill.md`, and use the template in `LLM_Assets/incose_template.md`. Also add some helpful tables and views in the model.

---

## 🛠️ Optional: Automated Validation Workflow (For Advanced Users)

If you have successfully installed the SysML v2 Java Validator and the `validate_model.py` script as outlined in the `Installation_Guide.md`, you can append the following instruction to **any** of the prompts above to enable self-correcting validation:

> **Validation Add-on:**
> "Please save the generated model to a file, and then use the `validate_model.py` script to validate the model. If the validator returns syntax errors, read `LLM_skills/fix_recipies.md` to learn how to fix the errors, and rewrite the model. Iterate automatically until the validator returns an exit code of 0."

## Train to deliver passengers

I want you to create an INCOSE discovery document and then a requirements document and then a logical SysMLv2 model and then a physical SysMLv2 model of a train to deliver passengers. The train should be able to operate autonomously on a track, accelerate, brake, and safely deliver passengers to their destinations. It should also have a camera and other sensors to detect obstacles on the tracks and maintain safe distances. Read and apply the rules in `LLM_skills/skill.md`, follow the process in `LLM_skills/methodology_skill.md`, and use the template in `LLM_Assets/incose_template.md`. Also add some helpful tables and views in the model.

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

## Simple Hobbyist Drone

I want you to create an new instance of 'incose_template.md' for the following project: A simple hobbyist drone that should be able to record video, fly, hover, and land based on user input from a cell phone app. Use research about hobby drones to create stakeholders, stakeholder concerns, stakeholder needs, operational scenarios, operational needs, operational concepts, and stakeholder expectations, use cases and verifyable requirements. Features and capabilities should be on par with a $500 consumer price point. Use that information to create a SysMLv2 text file based on the information about SysMLv2 from 'skill.md' that follows the package structure of OOSEM or MagicGrid process with a concept, and logical,and physical SysMLv2 model. Also add some helpful views (table and views that use expose to automatically render data as diagrams or tables) in the model. Read and apply the rules in 'skill.md', follow the process in 'methodology_skill.md', and use the template in 'incose_template.md'.

If the user detects an error in the model and gives you feedback, document and correct the error, going back through the process as needed. Record changes and rational in a "corrections_iteration#.md" file, where '#' is the iteration number.

## Simple Hobbyist Ebike

I want you to create an new instance of 'incose_template.md' for the following project: A simple hobbyist ebike that should be able to be ridden like a regular bike but also provide electric motor assist based on user input from a throttle, pedal assist sensor, and user selection of assist mode. The ebike should be able to operate on roads and trails, accelerate, brake, and safely assist the rider to their destination. It should also have a display to show speed, battery level, assist mode, and other relevant information. Features and capabilities should be on par with a $1500 consumer price point. Use research about hobby ebikes to create stakeholders, stakeholder concerns, stakeholder needs, operational scenarios, operational needs, operational concepts, and stakeholder expectations, use cases and verifyable requirements. Use that information to create a SysMLv2 text file based on the information about SysMLv2 from 'skill.md' that follows the package structure of OOSEM or MagicGrid process with a concept, and logical,and physical SysMLv2 model  Read and apply the rules in 'skill.md', follow the process in 'methodology_skill.md', and use the template in 'incose_template.md'. Also add some helpful views (table and views that use expose to automatically render data as diagrams or tables) in the model.

If the user detects an error in the model and gives you feedback, document and correct the error, going back through the process as needed. Record changes and rational in a "corrections_iteration#.md" file, where '#' is the iteration number.
