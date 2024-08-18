
import java.util.Map;
import java.util.Random;
import java.util.Scanner;

public class SL {

    public static void main(String[] args){

    //using hashmap for storing the snake and ladders values
    Map<Integer, Integer> snakes = Map.of(
    11, 1,
    28, 17,
    45, 30,
    67, 44,
    84, 59,
    99, 88
);
Map<Integer, Integer> ladders=Map.of(
    2, 38,
    9, 31,
    21, 42,
    36, 48,
    51, 67,
    71, 91,
    80, 97
);

    int playerPosition=0;
    
    while(playerPosition<100){
        System.out.println("1.Roll a die !\n 2.Exit");
        Scanner sc = new Scanner(System.in);
        int choice=sc.nextInt();

        if(choice==1){
        int dieValue = new Random().nextInt(1, 7);
        System.out.println("Got a Die value of  "+dieValue);
        playerPosition+=dieValue;
        
        //check if player lands on a snake
        if(snakes.containsKey(playerPosition)){
            playerPosition=snakes.get(playerPosition);
            System.out.println("SNAKE! Player moved to position "+playerPosition);
        }
        else if(ladders.containsKey(playerPosition)) {
            playerPosition=ladders.get(playerPosition);
            System.out.println("Ladder !! Player moved to "+playerPosition);
        }
        else{
            if(playerPosition<=100){
            System.out.println("Player moved to position "+playerPosition);
            }
        else{
        System.out.println("You won!");
    }
}
        }
    else{
        System.out.println("Exiting the game!");
        break;
    }
}
}
    
}
