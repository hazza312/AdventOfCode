open System

type hand = Rock | Paper | Scissors
type player_ending = Win | Draw | Lose
type result = player_ending * hand

let to_hand = function "A" | "X" -> Rock | "B" | "Y" -> Paper | _ -> Scissors

let loses_against = function 
    Rock -> Scissors | Paper -> Rock | Scissors -> Paper

let wins_against = function 
    Rock -> Paper | Paper -> Scissors | Scissors -> Rock
   
let get_score (player_ending, hand): int = 
    (match hand with Rock -> 1 | Paper -> 2 | Scissors -> 3)
    + (match player_ending with Win -> 6 | Draw -> 3 | _ -> 0)

let get_player_result = function  
    | a, b when a = b -> Draw, b
    | a, b when b = wins_against a -> Win, b
    | _, b -> Lose, b

let part1 (a, b): result = 
    (to_hand a, to_hand b) |> get_player_result

let part2 = function
    | a, "X" -> Lose, loses_against (to_hand a)
    | a, "Y" -> Draw, to_hand a
    | a, "Z" -> Win, wins_against (to_hand a)

let rec read_lines () = 
    match Console.ReadLine() with null -> [] | s -> s :: read_lines ()


let main =
    let split (line: string) = let [|a; b|] = line.Split " " in (a, b)
    let lines = read_lines () |> List.map split
    let do_result parser = List.map (parser >> get_score) lines |> List.sum |> printfn "%d"

    do_result part1  
    do_result part2

