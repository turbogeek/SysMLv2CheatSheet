package CheatSheetValidation {
    doc
    /* SysML v2 Cheat Sheet Code Snippets
     * Generated for validation in Cameo/Systems Modeler.
     *
     * This file contains examples from the cheat sheets, organized by category.
     * References to the SysML v2 Specification are included where applicable.
     */
    private import ScalarValues::*;
    private import ISQ::*;
    private import ISQBase::*;
    private import VerificationCases::*;
    package StructureExamples {
        doc
        /* =================================================================================
         * STRUCTURE CHEAT SHEET
         * =================================================================================
         * Examples corresponding to the 'Structure' cheat sheet. 
         */
        part def Vehicle {
            doc /* 1. Part Definition: Defining a structure block. */
            attribute m : mass;
            part engine : Engine;
        }
        part def Engine;
        part def Wheel;
        part car : Vehicle {
            doc /* 2. Part Usage: Using parts with constraints. */
            part wheels [4] : Wheel;
            part doors [2..4];
        }
        attribute def Status {
            doc /* 3. Attributes: Data properties. */
            attribute code : Integer;
        }
        part ecu {
            attribute id = "ECU-01";
        }
        part def Tank {
            doc /* 4. Ports: Interaction points. */
            port fuelOut : FuelInterface;
        }
        port def FuelInterface {
            out fuel : Gasoline;
        }
        item def Fuel;
        item def Gasoline :> Fuel;
        part def ElectricCar :> Vehicle {
            doc /* 7. Inheritance: Specialization. */
            part battery;
        }
        enum def Color {
            doc /* 8. Enumerations: Predefined values. */
            Red;
            Green;
            Blue;
        }
    }
    package ActionExamples {
        doc
        /* =================================================================================
         * ACTIONS CHEAT SHEET
         * =================================================================================
         * Examples corresponding to the 'Actions' cheat sheet. 
         */
        attribute def Speed;
        attribute def Result;
        action def Serve {
            doc /* 1. Action Definition: Reusable behavior spec. */
            in speed : Speed;
            out result : Result;
            first toss;
            then strike;
        }
        action toss;
        action strike;
        action playPoint {
            doc /* 2. Action Usage: Executing an action. */
            action serve : Serve;
            perform serve {
                doc /* Standard usage: */
                in speed = 60;
            }
            action serve2 : Serve;
            perform action serve2 {
                doc /* Explicit 'action' kind: */
            }
        }
        action decideStrategy {
            doc /* 3. Control Nodes: Decisions, merges, forks. */
            first evaluate;
            then decide checkWeakness;
            if weak == Backhand then targetBH;
            else targetForehand;
            merge endStrategy;
            action evaluate;
            action checkWeakness;
            action targetBH;
            action targetForehand;
            action endStrategy;
        }
        attribute weak;
        attribute Backhand;
        action def CalcSpin {
            doc /* 4. Parameters: Input, Output, Return. */
            in angle : Real;
            out rpm : Real;
        }
        action communicate {
            doc /* 5. Send/Accept Signal: Async communication. */
            attribute stopSig : Signal::Stop;
            send stopSig via pOut to ctl;
            attribute dataSig : Signal::Data;
            send dataSig via pOut to ctl;
            accept Signal::Resume;
        }
        part ctl;
        port pOut;
        package Signal {
            attribute def Stop;
            attribute def Resume;
            attribute def Data;
        }
        action process {
            doc /* 6. Succession: Ordering of actions. */
            first start;
            then process;
            then finish;
        }
        action start;
        action finish;
        action assignment {
            doc /* 7. Assignment: Setting values. */
            assign x := 42;
            assign y := x + 1;
        }
        attribute x : Integer;
        attribute y : Integer;
        action trigger {
            doc /* 8. Trigger: Reacting to events. */
            accept tick : Tick via clock;
            accept when t > 10.0;
        }
        attribute def Tick;
        part clock;
        attribute t : Real;
        action loops {
            doc /* 9. Loops: Iteration. */
            action loop1 while x < 10 {
                assign x := x + 1;
            }
        }
        requirement req2 {
            doc /* 7. Trace & Refine: Requirement relationships. */
        }
        part old_doc_item;
    }
    package ConnectionExamples {
        doc
        /* =================================================================================
         * CONNECTIONS CHEAT SHEET
         * =================================================================================
         * Examples corresponding to the 'Connections' cheat sheet. 
         */
        connection def DeviceConn {
            doc /* 1. Connection Definition: Defining connection types. */
            end hub : Hub;
            end device : Device;
        }
        part def Hub {
            port devPort;
        }
        part def Device {
            port hubPort;
        }
        part context {
            doc /* 1b. Connection Usage: Connecting parts. */
            connection c1 : DeviceConn {
                connect hub to device;
            }
            part hub : Hub;
            part device : Device;
        }
        part system {
            doc /* 2. Binding Connector: Equating two elements. */
            part a : A;
            part b : B;
            bind a.p1 = b.p2;
        }
        part def A {
            port p1;
        }
        part def B {
            port p2;
        }
        interface def IData {
            doc /* 3. Interface Connection: Flows within interfaces. */
            end source;
            end target;
            flow source to target;
        }
        action process_flow {
            doc /* 4. Succession Flow: Control/Data flow. */
            flow step1 to step2;
        }
        action step1;
        action step2;
    }
    package BehaviorExamples {
        doc
        /* =================================================================================
         * BEHAVIOR (STATES & CASES) CHEAT SHEET
         * =================================================================================
         * Examples corresponding to the 'States' and 'Cases' cheat sheets. 
         */
        state def PracticeSession {
            doc /* 1. State Definition: Define states and lifecycle actions. */
            entry;
            exit;
            state Idle;
            state Serving;
        }
        state def TrafficLight2 {
            doc /* 2. Transitions: Move between states on triggers. */
            entry;
            then Idle;
            state Idle;
            transition startServe first Idle accept Remote::Start do action log : Log { in msg = "Serving"; }
            then Serving;
            state Serving;
        }
        package Remote {
            attribute def Start;
        }
        action def Log { in msg : String; }
        state def Composite {
            doc /* 4. Composite States: States within states. */
            state Operational {
                entry;
                state Normal;
                state Maintenance;
            }
        }
        state def System parallel {
            doc /* 5. Parallel States: Concurrency. */
            state Power;
            state Connectivity;
        }
        use case def DriveCar {
            doc /* Cases: Functional goals. */
            subject vehicle : Vehicle;
            actor driver : Person;
            objective {
                doc /* Transport safely */
            }
        }
        part def Person;
        part def Vehicle;
        verification def TestBrakes {
            doc /* Verifying requirements. */
            subject vehicle : Vehicle;
            objective brakeReqCheck : BrakeRequirement {
                subject vehicle = TestBrakes::vehicle;
            }
            return verdict : VerdictKind;
        }
        requirement def BrakeRequirement {
            subject vehicle : Vehicle;
        }
        attribute stoppingDistance;
        analysis def FuelEconomy {
            doc /* Evaluating properties. */
            subject vehicle : Vehicle;
            objective fuelEconomyObjective {
                doc /* Estimate MPG */
            }
            return fuelEconomy : Real;
        }
        use case driveToWork : DriveCar {
            doc /* Instantiating a case. */
            subject;
            actor driver = me;
        }
        part me : Person;
    }
    package CalcExamples {
        doc
        /* =================================================================================
         * CONSTRAINTS & CALCS CHEAT SHEET
         * =================================================================================
         */
        calc def PowerCalc {
            in v : Voltage;
            in i : Current;
            return p : Power = v * i;
        }
        attribute def Voltage;
        attribute def Current;
        attribute def Power;
        calc p_motor : PowerCalc {
            in v = 12.0;
            in i = 5.0;
        }
        constraint def MassLimit {
            in m : Mass;
            in limit : Mass;
            m <= limit
        }
        attribute def Mass;
        constraint checkMass : MassLimit {
            in m = 500.0;
            in limit = 1000.0;
        }
        assert constraint {
            1 > 0
        }
        requirement def Safety {
            assume constraint {
                100 < 200
            }
            require constraint {
                50 < 100
            }
        }
    }
    package ActionPatternExamples {
        doc
        /* =================================================================================
         * ACTION PATTERNS CHEAT SHEET
         * =================================================================================
         */
        action patterns {
            while x < 10 {
                assign x := x + 1;
            }
            for i in 1..10 {}
            if x > 0 {
                assign x := 1;
            } else {
                assign x := 0;
            }
            accept sig : Signal;
            accept when x > 100;
            accept at schedule;
            accept after 10.0;
            action sendA send sig via p1;
            send sig via p1;
            send sig to target;
            part monitor {
                action sendReadingTo {
                    in part destination;
                    action sendReading send {
                        in payload;
                        in sender = monitor;
                        in receiver = destination;
                    }
                    send getReading.reading {
                        in sender = monitor;
                        in receiver = destination;
                    }
                }
                action getReading { out reading : SensorReading; }
            }
            attribute def SensorReading;
            fork f1;
            join j1;
            decide d1;
            merge m1;
        }
        attribute x : Integer;
        attribute i : Integer;
        attribute def Signal;
        attribute sig : Signal;
        attribute schedule;
        port p1;
        part target;
    }
    package StatePatternExamples {
        doc
        /* =================================================================================
         * STATE PATTERNS CHEAT SHEET
         * =================================================================================
         */
        state def Active {
            entry action logStart;
            do action maintain;
            exit action logEnd;
        }
        action def logStart;
        action def maintain;
        action def logEnd;
        state def Composite {
            entry;
            state Sub1;
            state Sub2;
            transition t1 first Sub1 then Sub2;
        }
        part def Vehicle {
            exhibit state opState ::> VehicleStates::operating;
        }
        state def VehicleStates {
            state operating;
        }
        state def Monitoring {
            state selfCheck;
            transition selfCheck accept tick do action check then selfCheck;
        }
        attribute def tick;
        action def check;
    }
    package ShorthandExamples {
        doc
        /* =================================================================================
         * SHORTHAND & ALTERNATIVES CHEAT SHEET
         * =================================================================================
         */
        part def Car :> Vehicle;
        part def Vehicle;
        part engine :> parts;
        part parts;
        attribute :>> ShorthandExamples::mass = 100;
        attribute mass;
        port p1 : ~Interface;
        port def Interface;
        attribute x = 1;
        attribute y := 2;
        attribute z default 3;
        part many [*];
        part one;
        part opt [0..1];
    }
    package ReferenceExamples {
        doc
        /* =================================================================================
         * REFERENCE CHEAT SHEET
         * =================================================================================
         */
        /* Multi-line
         * comment */
        doc /* Documentation */
        comment about part1 /* This is a comment about part1 */
        part part1;
    }
}
