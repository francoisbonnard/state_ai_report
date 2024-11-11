Change prompt

Open powershell

    notepad $PROFILE

add : 

    function prompt {
        "PS> "
    }


Pour avoir juste le dernier niveau : 

    function prompt {
    $currentDir = Split-Path -Leaf -Path (Get-Location)
    "$currentDir> "
    }
