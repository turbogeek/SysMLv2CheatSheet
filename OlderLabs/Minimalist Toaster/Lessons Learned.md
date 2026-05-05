# Lessons learned when generating the toaster model

Need to be sure that when a defining part is used, that the part def is defined in a reachable scope. For example this was incorrect because 'Toaster' was not defined in a reachable scope (caused by LLM hallucination in which the pattern of the subject types in use case was not defined or imported into the scope):

```sysml
    use case def ToastBread {
        subject toaster : Toaster;/* Incorrect unless 'Toaster is defined in a reachable scope */
        actor user : Person;
        actor bread : Bread;
        objective {
            doc /* User successfully transforms bread into toast using the system. */
        }
    }
```

In the same scope or a reachable imported package scope we need this added:

```sysml
    part def Toaster;
```

These are incorrect because the keyword 'requirement' is used before the name of the requirement usage (this is a sort of possible halucination when generating the SysMLv2 code with an LLM):

```sysml
            satisfy requirement Requirements::'Browning Time';
            satisfy requirement Requirements::'Electrical Insulation';
```

Should be:

````sysml
            satisfy Requirements::'Browning Time';
            satisfy Requirements::'Electrical Insulation';
```
When frame is used, the name of the concern should be used, do not use the keywork concern. For example the following is is incorrect:

````sysml
    frequirement <'REQ-SAFE-01'> 'Electrical Insulation' : RequirementTypes::SafetyRequirement {
            doc /* The toaster shall provide electrical insulation to prevent user contact with live parts. */
            frame concern StakeholderConcerns::'User Safety';
        }
```

should be:

```sysml
    requirement <'REQ-SAFE-01'> 'Electrical Insulation' : RequirementTypes::SafetyRequirement {
            doc /* The toaster shall provide electrical insulation to prevent user contact with live parts. */
            frame concern StakeholderConcerns::'User Safety';
        }
```
        
