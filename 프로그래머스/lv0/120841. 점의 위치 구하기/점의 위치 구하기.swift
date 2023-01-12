import Foundation

func solution(_ dot:[Int]) -> Int {
    var a:Int = 0
    if dot[0] > 0 {
        if dot[1] > 0 {
            a = 1
        } else {
            a = 4
        }
    } else {
        if dot[1] > 0 {
            a = 2
        } else {
            a = 3
        }
    }
    return a
}
