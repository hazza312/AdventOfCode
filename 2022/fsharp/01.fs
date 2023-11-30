let rec read_sums n =
    match System.Console.ReadLine() with 
    | null  -> []
    | ""    -> n :: read_sums 0
    | s     -> read_sums (n + int s)

let main =
    let sums = read_sums 0 |> List.sortDescending
    List.head sums |> printfn "%d"
    List.take 3 sums |> List.sum |> printfn "%d"
