use hashbrown::HashMap;

const ROW: u32 = 0b11111;
const COL: u32 = 0b100001000010000100001;

pub fn main() {
    let (nums, boards) = include_str!("../input.txt").split_once("\n\n").unwrap();

    let mut boards: Vec<(HashMap<u8, usize>, u32)> = boards
        .split("\n\n")
        .map(|b| {
            (
                b.split_ascii_whitespace()
                    .enumerate()
                    .map(|(i, n)| (n.parse().unwrap(), i))
                    .collect(),
                0,
            )
        })
        .collect();

    let (board, mark, num) = nums
        .split(',')
        .map(|n| n.parse().unwrap())
        .find_map(|n| {
            boards.iter_mut().find_map(|(b, m)| {
                b.get(&n)
                    .map(|i| *m |= 1 << *i)
                    .filter(|_| (0..5).any(|i| *m >> i & COL == COL || *m >> (i * 5) & ROW == ROW))
                    .map(|_| (b.clone(), *m, n))
            })
        })
        .unwrap();

    println!(
        "{}",
        board
            .into_iter()
            .map(|(n, i)| (mark >> i & 1 ^ 1) * n as u32 * num as u32)
            .sum::<u32>()
    );
}
