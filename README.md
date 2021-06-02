# Intro-to-RL-2021
Resources and Assignments for Introduction to Reinforcement Learning, Semester Project 2021

## Assignments

1. [Imitation Learning](ImitationLearning)

## General Instructions

### Using your Local Machine
1. Fork the repo on GitHub: Use the button at the top right.
2. Clone the project to your machine

    ```bash
    git clone https://github.com/${your_username}/Intro-to-RL-2021.git
    ```

3. Commit your solutions to your own branch: 

    Create a new branch by

    ```bash
    git checkout -b ${your_branch_name}
    ```

4. Push your work back up to your fork: 

    Navigate to the top-level repo directory and:

    ```bash
    git add .
    git commit -m "commit message"
    git push origin ${your_branch_name} 
    ```

5. Update the repo on your system by [setting an upstream](https://docs.github.com/en/github/collaborating-with-pull-requests/working-with-forks/configuring-a-remote-for-a-fork) to the `main` branch of **this** repository and then running -  
    ```bash
    git fetch upstream
    git checkout main
    git merge upstream/main
    ```

### Using Google Colab
You can alternatively do everything from Google Colab (less ideal), with the following changes to the above process.

1. Mount your Google Drive to Colab. 
    (Go to File Browser > Mount Drive when you run a notebook for the first time).

    If for some reason Drive doesn't automatically get mounted, add and run the following cell at the beginning of the notebook.

    ```python
    from google.colab import drive
    drive.mount('/content/drive')
    ```

2. Follow the above instructions **after** changing your working directory to `drive/MyDrive/${Preferred Directory}` by running
    ```iPython
    %cd drive/MyDrive/${Preferred Directory}
    ```
    Remember to start every command with a `!` (eg. `!git clone ${repo_link}`). 