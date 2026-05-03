package Flows {
    package Definitions {
        port def Outlet {
            out item fuelOut : Fuel;
            in item fuelIn : Fuel;
        }
        interface def 'Fuel Interface' {
            end : Outlet;
            end : ~Outlet;
            ref flow fuelSupply of Fuel from source.fuelOut to target.fuelOut;
            ref flow fuelReturn of Fuel from target.fuelOut to source.fuelOut;
        }
        item def Fuel;
        view definitions : DS_Views::SymbolicViews::gv;
    }
    part vehicle {
        part fuelTank {
            item fuel : Definitions::Fuel;
            port outlet : Definitions::Outlet;
            ref bind fuel = outlet.fuelOut;
        }
        part engine {
            item fuel : Definitions::Fuel;
            port outlet : ~Definitions::Outlet;
            ref bind fuel = outlet.fuelOut;
        }
        interface fuel_interface : Definitions::'Fuel Interface' connect fuelTank.outlet to engine.outlet;
        view 'interconnectivity of vehicle' : DS_Views::SymbolicViews::gv;
    }
    view flows : DS_Views::SymbolicViews::gv;
}
