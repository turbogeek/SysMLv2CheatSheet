package CoreTypes_3Enums {
    enum def TrafficColor {
        enum Red;
        enum Yellow;
        enum Green;
    }
    
    part trafficLight {
        attribute state : TrafficColor;
    }
    
    // Assigning an enum value
    part intersection {
        part light1 : trafficLight {
             attribute :>> state = TrafficColor::Red;
        }
    }
}