#include <string.h>
#include <stdint.h>
#include <iostream>
#include <cstring>
#include <stdio.h>


uint8_t crc8( uint8_t *addr, uint8_t len) {
      uint8_t crc=0;
      for(uint8_t i=0; i<len; i++){
         uint8_t inbyte = addr[i];
    
         for (uint8_t j=0;j<8;j++) {
             uint8_t mix = (crc ^ inbyte) & 0x01;
             crc >>= 1;
             if (mix) 
                crc ^= 0x8C;
         inbyte >>= 1;
      }
    }
   return crc;
}

int main(){


    std::string input = "String Test";
   
    char input_array[input.length() +1];

    strcpy(input_array, input.c_str());

    int result = crc8(reinterpret_cast<uint8_t*>(input_array), input.length());

    printf("%i", result);

}

