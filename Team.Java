import java.util.ArrayList;
import java.util.Random;

class Team {

  /* --------------------------
     ------- VARIABLES --------
     -------------------------- */

  // STATIC VARIABLE
  static int MAX_GAMES = 10;

  // INSTANCE VARIABLES
  String city;
  String mascot;
  int wins;
  int losses;
  int total_points;


  /* ------------------------
     ------- METHODS --------
     ------------------------ */

  // CONSTRUCTOR
  Team(String city, String mascot) {
    // Set the values of the instance variables here.
    // city and mascot should be set using the above parameters.
    // wins, losses, and total_points should be set to 0.
    this.city = city;
    this.mascot = mascot;
    this.wins = 0;
    this.losses = 0;
    this.total_points = 0;

  }

  // GETTERS
  // Write 5 getters, one for each instance variable.
  String getCity() {
    return this.city;
  }
  String getMascot() {
    return this.mascot;
  }
  int getWins() {
    return this.wins;
  }
  int getLosses() {
    return this.losses;
  }
  int getTotalPts() {
    return this.total_points;
  }

  // SETTERS
  // Write 5 setters, one for each instance variable.
  void setCity (String city) {
    this.city = city;
  }
  void setMascot (String mascot) {
    this.mascot = mascot;
  }
  void setWins (int wins) {
    this.wins = wins;
  }
  void setLosses (int losses) {
    this.losses = losses;
  }
  void setTotalPts (int total_points) {
    this.total_points = total_points;
  }

  // PLAY METHOD
  // Write an instance method called play() as follows.
  boolean play(Team t2) {

    // Here's how to generate a random number in the range [0, 100)
    double team1_points = Math.floor(Math.random() * 100);

    // Now generate the number for team2_points, following the above.
    double team2_points = Math.floor(Math.random() * 100);

    // There's a chance the two numbers will be the same. In that
    // case you'll want to regenerate the two numbers.
    // To do this, write a while loop whose condition is
    // team1_points is equal to team2_points,
    // and whose body is a repeat of the random number code above.

    while (team1_points == team2_points)
    {
      team1_points = Math.floor(Math.random() * 100);
      team2_points = Math.floor(Math.random() * 100);
    };
    //int t1PTS = team1_points.intValue();
    //int t2PTS = team2_points.intValue();
//t1PTS and t2PTS are the number of points scored by each team as ints instead
//of doubles.


    // Next write an if-else statement to determine who wins.
    // If team1_points > team2_points, the calling team (this) wins.
    // Otherwise, the argument team, t2, wins. Within the if-else:
    // * Increment each team's wins or losses variable.
    // * Increment each team's total_points variable.
    // * Return true if the calling team wins, otherwise false.
    if (team1_points > team2_points){
      return true;
      this.setWins(this.getWins()+1);
      t2.setLosses(t2.getLosses()+1);
      this.setTotalPts(this.getTotalPts() + t1PTS);
}
  else{
    return false;
    t2.setWins(t2.getWins()+1);
    this.setLosses(this.getLosses()+1);
    t2.setTotalPts(t2.getTotalPts() + t2PTS);
}
    // I am inserting this dummy return statement so the program
    // will compile. You should delete this line when you write
    // this method.
    //return true;

  }

  /* ------------------------
     ------- MAIN METHOD ----
     ------------------------ */

  // MAIN() METHOD
  public static void main (String[] args) {
    // Read in the first command line argument as an int.
    // If it is larger than the static variable MAX_GAMES,
    // quit the program by throwing an exception.
    // This is the code you can insert after the if-condition:
    // throw new IllegalArgumentException("Too many games requested.");
    String gamesPlayed = args[0];
    int numberOfGamesPlayed = Integer.parseInt (gamesPlayed);
    if (numberOfGamesPlayed > MAX_GAMES) {
      throw new IllegalArgumentException("Too many games requested.");
    }
    //gamesPlayed is the string of what is put into the command line argument
    //numberOfGamesPlayed converts this string into an integer

    // Here's an ArrayList of strings to keep track of who won each game.
    ArrayList<String> results = new ArrayList<String>();

    // Create two Team objects using your constructor.
    Team t1 = new Team ("Revere", "Patriot");
    Team t2 = new Team ("Boston", "Baldwin");

    // Have them play each other as many times as specified by the
    // command line argument. Each time they play, add the name of the
    // winner (city + mascot) to the ArrayList results.
    for (int i = 0; i<numberOfGamesPlayed; i++){
      boolean gameWinner = t2.Play (t2);
      args[i] = this.getCity() + this.getMascot();
    }


    // After the desired number of games, use a for-each loop with the
    // ArrayList to print out the name of the winning team for each game, e.g.,
    // "The Chestnut Hill Narwhals won!"
    for (this.getCity() : args)
    System.out.format("The %ss %ss won!" , this.getCity(), this.getMascot());

    // Using the getters for the wins and losses instance variables,
    // print out the record of wins and losses for each team, e.g.,
    // "Chestnut Hill Narwhals: 6 wins, 4 losses"


    // Print out which team won the whole series, e.g.,
    // "The Chestnut Hill Narwhals won the series."
    if (t1.getTotalPts() > t2.getTotalPts()){
      System.out.format ("The %s %ss won the series!" , t1.getCity(), t1.getMascot());
    }
    if (t1.getTotalPts() < t2.getTotalPts()){
      System.out.format ("The %s %ss won the series!" , t2.getCity(), t2.getMascot());
    }
    if (t1.getTotalPts() == t2.getTotalPts()){
      System.out.println ("It's a tie!");
    }
    //only one of these if statements will be true in the end,
    //so only one of these results will print

    // Print out the total number of points scored by each team, e.g.,
    // "The Chestnut Hill Narwhals scored 497 points."
    System.out.format ("The %s %ss scored %d points." ,t1.getCity(), t1.getMascot(), t1.getTotalPts());
    System.out.format ("The %s %ss scored %d points." ,t2.getCity(), t2.getMascot(), t2.getTotalPts());
  }

}
