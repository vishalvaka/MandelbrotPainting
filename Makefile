# Compiler settings - Can be customized.
CC=g++
MPICC=mpicxx

# Program names
SERIAL_TARGET=mandelbrot-serial
MPI_TARGET=mandelbrot-mpi

# Source files
SERIAL_SRC=mandelbrot-serial.cc
MPI_SRC=mandelbrot-mpi.cc

# Compiler flags
CFLAGS=-O3 -march=native
MPIFLAGS=$(CFLAGS)

# Default target executed when no arguments are given to make.
default: mpi

# Target for building serial version
serial:
	$(CC) $(CFLAGS) -o $(SERIAL_TARGET) $(SERIAL_SRC)

# Target for building MPI version
mpi:
	$(MPICC) $(MPIFLAGS) -o $(MPI_TARGET) $(MPI_SRC)

# Target for building all versions
all: serial mpi

# Target for cleaning up the project
clean:
	rm -f $(SERIAL_TARGET) $(MPI_TARGET) *.pnm *.png
