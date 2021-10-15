#include "types.h"

#define csr_tohost(csr_val) { \
    asm volatile ("csrw 0x51e,%[v]" :: [v]"r"(csr_val)); \
}

#define COUNTER_RST (*((volatile uint32_t*) 0x80000018))
#define CYCLE_COUNTER (*((volatile uint32_t*)0x80000010))
#define INSTRUCTION_COUNTER (*((volatile uint32_t*)0x80000014))

#define GPIO_FIFO_EMPTY (*((volatile uint32_t*)0x80000020) & 0x01)
#define GPIO_FIFO_DATA (*((volatile uint32_t*)0x80000024))
#define SWITCHES (*((volatile uint32_t*)0x80000028) & 0x03)
#define LED_CONTROL (*((volatile uint32_t*)0x80000030))
