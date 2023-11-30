open System

type filesystem = Folder of int * string * list<filesystem> | File of string * int 
let size = function File(_, n) -> n | Folder(n, _, _) -> n

let rec read_input () = 
    match Console.ReadLine() with
    | null -> [] 
    | s -> match s.Split " " with 
            | [|"$"; "cd"; "/"|]
            | [|"$"; "ls"|]
            | [|"dir"; _|]  -> read_input () 
            | [|"$"; "cd"; ".."|] -> []
            | [|"$"; "cd"; s|] -> Folder(0, s, read_input ()) :: read_input ()
            | [|n; f|] -> File(f, (int n)) :: read_input ()

let rec withFolderSizes = function 
| Folder(_, s, children) -> 
    let sizedChildren = (List.map withFolderSizes children)
    Folder(List.sumBy size sizedChildren, s, sizedChildren)
| file -> file

let rec countFolders = function 
| File(_,_) -> 0
| Folder(n, _, children) -> (if n <= 100000 then n else 0) + List.sumBy countFolders children

let rec minFolderBiggerThan over = function 
| File(_, _) -> Int32.MaxValue 
| Folder(n, _, children) ->
    let smallestChild = List.map (minFolderBiggerThan over) children |> List.min
    if n >= over && n < smallestChild then n else smallestChild


let main = 
    let root = Folder(0, "root", read_input ()) |> withFolderSizes
    root |> countFolders |> printfn "%d"

    let used_space = size root 
    let required =  used_space + 30000000 - 70000000
    minFolderBiggerThan required root |> printfn "%d" 
