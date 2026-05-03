package 'Use Case' {
    package 'Use Case Example no.1 (no reuse)' {
        package 'Exchange Items' {
            item def 'Mission Data';
            item def 'FA&S Kit';
        }
        view 'example no.1' : DS_Views::SymbolicViews::gv;
        part 'drone in search and rescue mission' {
            include use case 'find person in distress' {
                subject :> 'search drone' {
                    perform 'fly to destination';
                    perform 'fly by search \npattern';
                    perform 'drop fa&s kit';
                }
                actor :> 'ground control station' {
                    perform 'start mission';
                }
                actor :> 'person in distress' {
                    perform 'get help';
                }
                action 'start mission' { out md; }
                action 'fly to destination' { in md; }
                action 'get help' { in fas; }
                action 'fly by search \npattern';
                ref first 'fly to destination' then 'fly by search \npattern';
                ref succession flow of 'Exchange Items'::'Mission Data' from 'start mission'.md to 'fly to destination'.md;
                ref succession flow of 'Exchange Items'::'FA&S Kit' from 'drop fa&s kit'.fas to 'get help'.fas;
                ref first start then 'start mission';
                ref first 'get help' then done;
                action 'drop fa&s kit' { out fas; }
                ref first 'fly by search \npattern' then 'drop fa&s kit';
            }
            part 'ground control station';
            part 'person in distress';
            part 'search drone';
            ref flow of 'Exchange Items'::'Mission Data' {
                end ::> 'ground control station';
                end ::> 'search drone';
            }
            ref flow of 'Exchange Items'::'FA&S Kit' {
                end ::> 'search drone';
                end ::> 'person in distress';
            }
        }
    }
    package 'Use Case Example no.2 (ligth reuse)' {
        use case 'provide value using drone' {
            subject SOI;
            actor operator;
            objective {
                doc /* interaction between subject and actors must provide value.*/
            }
            actor receiver;
        }
        view 'example no.2' : DS_Views::SymbolicViews::gv;
        part 'drone in cargo delivery mission' {
            ref flow of 'Exchange Items'::'Mission Data' {
                end ::> 'central delivery station';
                end ::> 'delivery drone';
            }
            ref flow of 'Exchange Items'::Goods {
                end ::> 'delivery drone';
                end ::> customer;
            }
            part 'delivery drone';
            part 'central delivery station';
            part customer;
            include use case 'provide goods to customer' ::> 'provide value using drone' {
                subject :>> SOI :> 'delivery drone' {
                    perform 'fly to destination';
                    perform 'drop cargo';
                }
                actor :>> operator :> 'central delivery station' {
                    perform 'start mission';
                }
                actor :>> receiver :> customer {
                    perform 'get cargo';
                }
                action 'start mission' { out md; }
                action 'fly to destination' { in md; }
                ref succession flow of 'Exchange Items'::'Mission Data' from 'start mission'.md to 'fly to destination'.md;
                ref first start then 'start mission';
                action 'drop cargo' { out gd; }
                ref first 'fly to destination' then 'drop cargo';
                action 'get cargo' { in gd; }
                ref succession flow of 'Exchange Items'::Goods from 'drop cargo'.gd to 'get cargo'.gd;
            }
        }
        part 'drone in search and rescue mission' {
            include use case 'find person in distress' ::> 'provide value using drone' {
                subject :> 'search drone' :>> SOI {
                    perform 'fly to destination';
                    perform 'fly by search \npattern';
                    perform 'drop fa&s kit';
                }
                actor :> 'ground control station' :>> operator {
                    perform 'start mission';
                }
                actor :> 'person in distress' :>> receiver {
                    perform 'get help';
                }
                action 'start mission' { out md; }
                action 'fly to destination' { in md; }
                action 'get help' { in fas; }
                action 'fly by search \npattern';
                ref first 'fly to destination' then 'fly by search \npattern';
                ref succession flow of 'Exchange Items'::'Mission Data' from 'start mission'.md to 'fly to destination'.md;
                ref succession flow of 'Exchange Items'::'FA&S Kit' from 'drop fa&s kit'.fas to 'get help'.fas;
                ref first start then 'start mission';
                ref first 'get help' then done;
                action 'drop fa&s kit' { out fas; }
                ref first 'fly by search \npattern' then 'drop fa&s kit';
            }
            part 'ground control station';
            part 'person in distress';
            part 'search drone';
            ref flow of 'Exchange Items'::'Mission Data' {
                end ::> 'ground control station';
                end ::> 'search drone';
            }
            ref flow of 'Exchange Items'::'FA&S Kit' {
                end ::> 'search drone';
                end ::> 'person in distress';
            }
        }
        package 'Exchange Items' {
            item def 'Mission Data';
            item def 'FA&S Kit';
            item def Goods;
        }
    }
    package 'Use Case Example no.3 (full reuse)' {
        use case 'provide value using drone' {
            subject SOI {
                perform 'fly to destination';
            }
            actor operator {
                perform 'start mission';
            }
            objective {
                doc /* interaction between subject and actors must provide value.*/
            }
            actor receiver;
            action 'start mission' { out md; }
            action 'fly to destination' { in md; }
            ref succession flow of 'Exchange Items'::'Mission Data' from 'start mission'.md to 'fly to destination'.md;
            ref first start then 'start mission';
        }
        part 'drone in cargo delivery mission' {
            ref flow of 'Exchange Items'::'Mission Data' {
                end ::> 'central delivery station';
                end ::> 'delivery drone';
            }
            ref flow of 'Exchange Items'::Goods {
                end ::> 'delivery drone';
                end ::> customer;
            }
            part 'delivery drone';
            part 'central delivery station';
            part customer;
            include use case 'provide goods to customer' ::> 'provide value using drone' {
                subject :>> SOI :> 'delivery drone' {
                    perform 'drop cargo';
                }
                actor :>> operator :> 'central delivery station';
                actor :>> receiver :> customer {
                    perform 'get cargo';
                }
                action 'drop cargo' { out gd; }
                action 'get cargo' { in gd; }
                ref succession flow of 'Exchange Items'::Goods from 'drop cargo'.gd to 'get cargo'.gd;
                ref first 'fly to destination' then 'drop cargo';
                ref first 'get cargo' then done;
            }
        }
        part 'drone in search and rescue mission' {
            include use case 'find person in distress' ::> 'provide value using drone' {
                subject :> 'search drone' :>> SOI {
                    perform action;
                    perform 'fly by search \npattern';
                    perform 'drop fa&s kit';
                }
                actor :> 'ground control station' :>> operator {
                    perform action;
                }
                actor :> 'person in distress' :>> receiver {
                    perform 'get help';
                }
                action 'get help' { in fas; }
                action 'fly by search \npattern';
                ref succession flow of 'Exchange Items'::'FA&S Kit' from 'drop fa&s kit'.fas to 'get help'.fas;
                ref first 'get help' then done;
                action 'drop fa&s kit' { out fas; }
                ref first 'fly by search \npattern' then 'drop fa&s kit';
                ref first 'fly to destination' then 'fly by search \npattern';
            }
            part 'ground control station';
            part 'person in distress';
            part 'search drone';
            ref flow of 'Exchange Items'::'Mission Data' {
                end ::> 'ground control station';
                end ::> 'search drone';
            }
            ref flow of 'Exchange Items'::'FA&S Kit' {
                end ::> 'search drone';
                end ::> 'person in distress';
            }
        }
        package 'Exchange Items' {
            item def 'Mission Data';
            item def 'FA&S Kit';
            item def Goods;
        }
        view 'example no.3' : DS_Views::SymbolicViews::gv;
    }
    view 'use cases' : DS_Views::SymbolicViews::gv;
}
