package Picklebot_Structure {
    part def <'ser-1234'> WheelAssembly;
    alias WA for 'ser-1234';
    comment about 'ser-1234' /* Look, an alias*/
    part chassis {
        doc /* Naming convention? Never heard of him. */
        part Bartholomew : 'ser-1234';
        part Esmeralda : 'ser-1234';
        part Barnaby_The_Swift : 'ser-1234' {
            comment about Barnaby_The_Swift /* also use the short name for fun! */
            doc /* I think this one looks like a Chauncey. */
        }
        part Chauncey : 'ser-1234';
    }
}
