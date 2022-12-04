open System

type hand = Rock | Paper | Scissors
type outcome = Win | Draw | Lose

let to_hand = function "A" | "X" -> Rock | "B" | "Y" -> Paper | _ -> Scissors

let other_hand_for_outcome outcome h = match outcome with 
| Lose -> (match h with Rock -> Scissors | Paper -> Rock | Scissors -> Paper)
| Win -> (match h with Rock -> Paper | Paper -> Scissors | Scissors -> Rock)
| Draw -> h

let get_score (outcome, hand): int = 
    (match hand with Rock -> 1 | Paper -> 2 | Scissors -> 3)
    + (match outcome with Win -> 6 | Draw -> 3 | _ -> 0)

let game_result (a', b') = 
    let a, b = (to_hand a', to_hand b')
    if a = b then Draw, b
    else if other_hand_for_outcome Win a = b then Win, b
    else Lose, b

let forced_outcome (a, x) = 
    let result = match x with "X" -> Lose | "Y" -> Draw | "Z" -> Win 
    result, other_hand_for_outcome result (to_hand a)

let rec read_lines () = 
    match Console.ReadLine() with null -> [] | s -> s :: read_lines ()


let main =
    let split (line: string) = let [|a; b|] = line.Split " " in (a, b)
    let lines = read_lines () |> List.map split
    let sum_scores f = List.fold (fun acc i -> acc + get_score (f i)) 0 lines
    
    sum_scores game_result  |> printfn "%d"
    sum_scores forced_outcome |> printfn "%d"
