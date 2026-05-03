package Actions {
    package 'Drone Model' {
        private import ScalarValues::**;
        part 'drone in any mission' {
            part drone {
                perform 'run mission'.proceed;
                perform 'run mission'.'check battery';
            }
            part 'mission control center' {
                perform 'run mission'.'start mission';
                perform 'run mission'.'evaluate weather conditions';
                perform 'run mission'.'evaluate battery range';
                perform 'run mission'.'abort mission';
            }
            perform action 'run mission' {
                action 'start mission' { out destination; }
                action 'evaluate weather conditions' {
                    in attribute temp;
                    in attribute speed;
                }
                action proceed;
                ref first proceed then done;
                action 'measure temperature' { out attribute temp; }
                action 'measure wind speed' { out attribute speed; }
                fork __unnamed1;
                ref first __unnamed1 then 'measure temperature';
                ref first __unnamed1 then 'measure wind speed';
                join __unnamed2;
                ref first 'start mission' then __unnamed1;
                ref first 'measure temperature' then __unnamed2;
                ref first 'measure wind speed' then __unnamed2;
                ref first __unnamed2 then 'evaluate weather conditions';
                decide __unnamed3;
                ref first 'evaluate weather conditions' then __unnamed3;
                first __unnamed3 if "weather is good" then __unnamed4;
                ref succession flow 'measure temperature'.temp to 'evaluate weather conditions'.temp;
                ref succession flow 'measure wind speed'.speed to 'evaluate weather conditions'.speed;
                view 'drone in any mission' : DS_Views::SymbolicViews::gv;
                action 'check battery' { out attribute 'battery level'; }
                ref first __unnamed1 then 'check battery';
                action 'evaluate battery range' {
                    in attribute 'battery level';
                    in destination;
                }
                ref succession flow 'check battery'.'battery level' to 'evaluate battery range'.'battery level';
                ref succession flow 'start mission'.destination to 'evaluate battery range'.destination;
                decide __unnamed5;
                ref first 'evaluate battery range' then __unnamed5;
                ref first __unnamed4 then proceed;
                first __unnamed5 if "level sufficient" then __unnamed4;
                merge __unnamed6;
                first __unnamed3 if "weather is bad" then __unnamed6;
                first __unnamed5 if "level insufficient" then __unnamed6;
                ref first start then 'start mission';
                action 'abort mission';
                ref first __unnamed6 then 'abort mission';
                ref first 'abort mission' then done;
                merge __unnamed4;
            }
            part 'weather station' {
                perform 'run mission'.'measure temperature';
                perform 'run mission'.'measure wind speed';
            }
        }
        part 'drone in delivery mission' :> 'drone in any mission' {
            view 'drone in delivery mission' : DS_Views::SymbolicViews::gv;
            perform action 'run delivery mission' :>> 'run mission' {
                action 'start delivery mission' :>> 'start mission' {
                    out ref;
                    out cargoID : String;
                }
                action 'prepare package \nto be lift' {
                    in cargoID : String;
                    out cargo;
                }
                ref succession flow 'start delivery mission'.cargoID to 'prepare package \nto be lift'.cargoID;
                ref first start then 'start delivery mission';
                action 'deliver package' :>> proceed {
                    in item cargo;
                    action loadCargo { in item cargo; }
                    action takeOff;
                    action deliverCargo;
                    perform action navigateToTarget ::> 'Actions Library'::navigateFromAtoB;
                    perform action navigateToHome ::> 'Actions Library'::navigateFromAtoB;
                    ref bind cargo = loadCargo.cargo;
                    ref first loadCargo then takeOff;
                    ref first start then loadCargo;
                    ref first takeOff then navigateToTarget;
                    ref first navigateToTarget then deliverCargo;
                    ref first deliverCargo then navigateToHome;
                    ref first navigateToHome then done;
                }
                ref succession flow 'prepare package \nto be lift'.cargo to 'deliver package'.cargo;
            }
            part 'distribution center' {
                perform 'run delivery mission'.'prepare package \nto be lift';
                perform action;
            }
            part :>> 'mission control center' {
                perform 'run delivery mission'.'start delivery mission';
            }
            part :>> drone {
                perform 'run delivery mission'.'deliver package' {
                    view 'deliver package' : DS_Views::SymbolicViews::gv;
                    view 'deliver package (multiple calls to action)' : DS_Views::SymbolicViews::gv;
                }
                part propulsionSystem {
                    perform 'deliver package'.takeOff;
                }
                part navigationSystem {
                    perform 'deliver package'.navigateToTarget;
                    perform 'deliver package'.navigateToHome;
                }
                part cargoBay {
                    perform 'deliver package'.loadCargo;
                    perform 'deliver package'.deliverCargo;
                }
            }
            view 'decomposition of actions and structure' : DS_Views::SymbolicViews::gv;
        }
        view 'behavior and structure mapping' : DS_Views::SymbolicViews::gv;
    }
    package 'Actions Library' {
        action navigateFromAtoB {
            view navigateFromAtoB : DS_Views::SymbolicViews::gv;
            action initialize;
            action 'check GPS';
            ref first initialize then 'check GPS';
            action 'set destination';
            ref first 'check GPS' then 'set destination';
            action 'calculate route';
            ref first 'set destination' then 'calculate route';
            action 'monitor flight path';
            ref first 'calculate route' then 'monitor flight path';
            action 'destination reached';
            ref first 'monitor flight path' then 'destination reached';
            ref first 'destination reached' then done;
            ref first start then initialize;
        }
    }
    view 'actions and swimlanes' : DS_Views::SymbolicViews::gv;
}
