# Checkpoint 1: 3 Stage Pipelined RISC-V CPU
The first checkpoint in this project is designed to guide the development of a three-stage pipelined RISC-V CPU that will be used as a base system in subsequent checkpoints.

**TODO TODO TODO INCLUDE DIAGRAM OF PROJECT OVERVIEW**
%\begin{figure}[hbt]
%\begin{center}
%  \includegraphics[width=0.7\textwidth]{sp21_overview.pdf}
%  \caption{High-level overview of the full system}
%  \label{fig:sys_overview}
%\end{center}
%\end{figure}

%The green (RISC-V core) block on the diagram is the focus of the first and second checkpoints.
%The third checkpoint will add audio and IO components in blue.
%Finally, the fourth checkpoint will implement the power management unit in red.

## Setting up Your Repository
The project skeleton files are available on Github.
The suggested way for initializing your repository with the skeleton files is as follows:

```bash
git clone git@github.com:EECS150/project_skeleton_fa21.git
cd project_skeleton_fa21
git remote add my-repo git@github.com:EECS150/fa21_teamXX.git
git push my-repo master
```

Then reclone your repo and add the skeleton repo as a remote:
\begin{minted}[tabsize=2]{bash}
  cd ..
  rm -rf project_skeleton_sp21
  git clone git@github.com:EECS150/sp21_teamXX.git
  cd sp21_teamXX
  git remote add staff git@github.com:EECS150/project_skeleton_sp21.git
\end{minted}

To pull project updates from the skeleton repo, run \verb|git pull staff main|.

To get a team repo, fill the \href{https://docs.google.com/forms/d/1hOJek4q_Z6SokflpH17gOESGGCXmY1VfdJ5VLMNku1U}{Google form} with your team information (names, Github logins). Only one person in a team is required to fill the form.

\textbf{You should check frequently for updates to the skeleton files.} Whenever you resume your work on the project,
it is highly suggested that you do git pull from the skeleton repo to get the latest update.
Update announcements will be posted to Piazza.

\subsection{Integrate Designs from Labs} \label{sec:past_designs}
You should copy some modules you designed from the labs.
We suggest you keep these with the provided source files in \verb|hardware/src/io_circuits| (overwriting any provided skeletons).

\textbf{Copy these files from the labs:}
\begin{minted}{bash}
  debouncer.v
  synchronizer.v
  edge_detector.v
  fifo.v
  uart_transmitter.v
\end{minted}
