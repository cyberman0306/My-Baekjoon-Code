import Foundation

func solution(_ strlist:[String]) -> [Int] {
    var a = [Int]()
    var b: String = ""
    var c: Int = 0
    for i in strlist {
        b = ""
        b += i
        c = b.count
        a.append(c)
    }
    return a
}
