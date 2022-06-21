import numpy as np
from ortools.linear_solver import pywraplp
from random import randint

def gen_input(n_machine, n_job, max_task, min_task,max_time,min_time):
    job_n_tasks = [0]*n_job
    job_task_machine=[[] for i in range(n_job)]
    job_task_time=[[] for i in range(n_job)]
    for i in range(n_job):
        job_n_tasks[i] = randint(min_task,max_task)
    for i in range(n_job):
        for j in range(job_n_tasks[i]):
            job_task_machine[i].append(randint(0,n_machine-1))
            job_task_time[i].append(randint(min_time,max_time))
    return job_n_tasks, job_task_machine, job_task_time

n_jobs=3
n_machine=3
max_task=3
min_task=3
max_time=10
min_time=1
INF = 9999999
V= 10000

job_n_task, r,d = gen_input(n_machine,n_jobs,max_task,min_task,max_time,min_time)

solver = pywraplp.Solver.CreateSolver('SCIP')
x = [[0] for i in range(n_jobs)]
for j in range(n_jobs):
    x[j]=[solver.NumVar(0,INF,"x[%d,%d]"%(j,i)) for i in range(job_n_task[j])]
   
z = [[] for j in range(n_jobs)]
for j in range(n_jobs):
    z[j] = [[] for i in range(job_n_task[j])]
    for i in range(job_n_task[j]):
        z[j][i] = [[] for j2 in range(n_jobs)]
        for j2 in range(n_jobs):
            z[j][i][j2] =[solver.IntVar(0,1,"z[%d,%d,%d,%d]"%(j,i,j2,i2)) for i2 in range(job_n_task[j2])]

y = solver.NumVar(0,INF,"Completion Time")

for j in range(n_jobs):
    for i in range(job_n_task[j]-1):
        constr1 = solver.Constraint(d[j][i],INF,'constr1[%d][%d]'%(j,i))
        constr1.SetCoefficient(x[j][i+1],1)
        constr1.SetCoefficient(x[j][i],-1)

for j1 in range(n_jobs):
    for i1 in range(job_n_task[j1]):
        for j2 in range(n_jobs):
            for i2 in range(job_n_task[j2]):
                if r[j1][i1]==r[j2][i2]:
                    constr2 = solver.Constraint(0,1,"constr2[%d][%d][%d][%d]"%(j1,i1,j2,i2))
                    constr2.SetCoefficient(z[j1][i1][j2][i2],1)
                    constr2.SetCoefficient(z[j2][i2][j1][i1],1)

for j1 in range(n_jobs):
    for i1 in range(job_n_task[j1]):
        for j2 in range(n_jobs):
            for i2 in range(job_n_task[j2]):
                if r[j1][i1]==r[j2][i2]:
                    constr3 = solver.Constraint(d[j1][i1]-V,INF,"constr3[%d][%d][%d][%d]"%(j1,i1,j2,i2))
                    constr3.SetCoefficient(x[j2][i2],1)
                    constr3.SetCoefficient(x[j1][i1],-1)
                    constr3.SetCoefficient(z[j1][i1][j2][i2],-V)
for j in range(n_jobs):
    constr4 = solver.Constraint(d[j][job_n_task[j]-1],INF,"constr4[%d]"%j)
    constr4.SetCoefficient(y,1)
    constr4.SetCoefficient(x[j][job_n_task[j]-1],-1)

objective = solver.Objective()
objective.SetCoefficient(y,1)
objective.SetMinimization()
status = solver.Solve()