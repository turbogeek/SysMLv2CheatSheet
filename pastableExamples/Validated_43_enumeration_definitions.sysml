package EnumerationTests;

// Test enumeration definitions

enum def Status {
    enum Pending;
    enum Active;
    enum Completed;
    enum Failed;
}

enum def Priority {
    enum Low;
    enum Medium;
    enum High;
    enum Critical;
}

part def Task {
    attribute status : Status;
    attribute priority : Priority;
}

part def Workflow {
    part taskA : Task {
        :>> status = Status::Pending;
        :>> priority = Priority::High;
    }

    part taskB : Task {
        :>> status = Status::Active;
        :>> priority = Priority::Medium;
    }

    assert constraint {
        taskA.status == Status::Pending or
        taskA.status == Status::Active
    }
}

enum def Color {
    enum Red;
    enum Green;
    enum Blue;
    enum Yellow;
}

attribute systemColor : Color = Color::Blue;
