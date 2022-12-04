open System 

let parseRange (l: string) = 
    let [| a; b |] = l.Split "-" in Set.ofSeq [int a..int b]

let parseLine (s: string) = 
    let [| a; b |] = s.Split "," |> Array.map parseRange in (a, b)

let rec readLines () = 
    match Console.ReadLine() with null -> [] | s -> s :: readLines ()

let oneIsStrictSuperset (a, b) = 
    Set.intersect a b |> Set.count = Math.Min ((Set.count a), (Set.count b))

let hasItemsInCommon (a, b) = 
    not (Set.intersect a b |> Set.isEmpty)


let main = 
    let parsed = readLines () |> List.map parseLine
    let countWhen f = List.fold (fun acc i -> acc + if (f i) then 1 else 0) 0

    countWhen oneIsStrictSuperset parsed |> printfn "%d"
    countWhen hasItemsInCommon parsed |> printfn "%d"
