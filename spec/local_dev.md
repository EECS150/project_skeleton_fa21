# Local Development
You can build the project on your laptop but there are a few dependencies to install.
In addition to Vivado and Icarus Verilog, you need a RISC-V GCC cross compiler and an `elf2hex` utility.

## Vivado
Download the Windows exe installer or the Linux bin installer [directly from Xilinx](https://www.xilinx.com/support/download.html) for Vivado ML Edition 2021.1.
You will need to create a (free) Xilinx account.

For Windows, just install Vivado like any other program.
For Linux, set the execute bit `chmod +x Xilinx_Unified_2021.1_0610_2318_Lin64.bin` and execute the script `./Xilinx_Unified_2021.1_0610_2318_Lin64.bin`.

In the installer, select "Vivado" in the "Select Product to Install" screen, pick "Vivado ML Standard" in the "Select Edition to Install" screen, and check the boxes to only install support for the Zynq-7000 part, to minimize disk usage.

*Note:* If you have an ARM-based M1 Macbook, you cannot install Vivado, but you can still run RTL simulations on your laptop with Icarus Verilog.

## Icarus Verilog + gtkwave
You can install Icarus Verilog and gtkwave on your laptop via Homebrew ([iverilog](https://formulae.brew.sh/formula/icarus-verilog), [gtkwave](https://formulae.brew.sh/cask/gtkwave)) or a package manager with Linux or WSL.

## RISC-V GCC Toolchain
Download and extract the package from [SiFive's software website](https://www.sifive.com/software) under "Prebuilt RISC‑V GCC Toolchain and Emulator".
You should download the appropriate package for "GNU Embedded Toolchain — v2020.12.8".

Extract the package into `/opt/riscv` or any other directory.
Set the envvar `$RISCV` to point to the extracted directory.
Add the `bin` directory inside the extracted directory to your `$PATH`.

Make sure you can run
```bash
riscv64-unknown-elf-gcc -v
```

## elf2hex
```bash
git clone git@github.com:sifive/elf2hex.git
cd elf2hex
autoreconf -i
./configure --target=riscv64-unknown-elf --prefix=/opt/riscv
make
make install
```

Make sure you can run
```bash
riscv64-unknwon-elf-elf2hex
```
