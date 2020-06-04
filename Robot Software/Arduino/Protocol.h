class Protocol{
    public:


    private:
        uint8_t crc8( uint8_t *addr, uint8_t len);

}

struct Packet{
    uint8_t angle;
    uint8_t joint_index;
    uint8_t crc;

}