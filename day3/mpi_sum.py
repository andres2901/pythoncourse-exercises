from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

send_val = np.array(rank, dtype=int)
recv_val = np.array(0, dtype=int)

comm.Reduce(send_val, recv_val, op=MPI.SUM, root=0)

if rank == 0:
    print(f"The total sum of all ranks is: {recv_val}")
