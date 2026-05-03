package SuccessionFlowTests;

// Test succession and flow connections

action def Workflow {
    action step1 {
        out result1 : Real;
    }

    action step2 {
        in input2 : Real;
        out result2 : Real;
    }

    action step3 {
        in input3 : Real;
    }

    // Succession with first...then
    first step1;
    then step2;
    then step3;

    // Flow connections
    succession step1 then step2;
    flow step1.result1 to step2.input2;
    flow step2.result2 to step3.input3;
}

action def ParallelWorkflow {
    action initialize;
    action processA;
    action processB;
    action finalize;

    first initialize;
    then fork (processA, processB);
    then join finalize;
}
