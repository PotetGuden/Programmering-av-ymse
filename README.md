# testing1
Testing github

Ting kan være litt rotete, se bort ifra de :)


Git commands


    //Laster ned en copy til pcen din, av den url du setter inn
    git clone "url til repository"

    // cd - change-directory, bytter directory i bash/cmd. (kan også bruke cd .. for å hoppe opp en mappe)
    cd "navn på mappe man vil til"

    //lister alle mapper under den mappen man er i, sjekk over for å teste litt.
    ls

    //Sjekker status på alle evt endringer
    git status

    //For å gjøre klar filer
    git add . (for å legge til alle filer), eller så kan man bare skrive navn på filene, feks git add README.md GitTest.htm

    //bruk -m for å legge til en message som er viktig!
    git commit -m " forklarende melding om hva man har gjort "

    //pusher filene inn til github.com, (master er branchen jeg vil bruke, kunne brukt en annen branch, men da må man skrive navn på den)
    git push origin master

    //lister alle branches
    git branch

    //for å lage en branch
    git branch "navn"

