package ActorStakeholderTests;

// Test actor and stakeholder definitions

actor def User {
    doc /* End user of the system */
}

actor def Administrator {
    doc /* System administrator */
}

actor def ExternalSystem {
    doc /* External interfacing system */
}

stakeholder def Customer {
    doc /* Paying customer */

    concern 'Cost' {
        doc /* Minimize total cost of ownership */
    }

    concern 'Usability' {
        doc /* System must be easy to use */
    }
}

stakeholder def Regulator {
    doc /* Regulatory authority */

    concern 'Compliance' {
        doc /* System must meet regulatory requirements */
    }
}

use case def SystemOperation {
    subject system : MainSystem;
    actor user : User;
    actor admin : Administrator;
}

part def MainSystem {
    doc /* Main system being designed */
}

// Requirements from stakeholders
requirement def CustomerRequirement {
    stakeholder customer : Customer;

    doc /* Requirements derived from customer concerns */

    satisfy concern customer.Cost;
    satisfy concern customer.Usability;
}

requirement costReq : CustomerRequirement {
    doc /* Total cost of ownership must be under $10M */
}
