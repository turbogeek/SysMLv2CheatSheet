package TestViews {
    part def Car;
    part myCar : Car;
    
    view carDiagram {
        expose myCar::**;
        render rendering asTable {
            view :>> 'Declared Name';
        }
    }
}
