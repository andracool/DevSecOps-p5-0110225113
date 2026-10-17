"""Antarmuka command line CowokKit."""
import argparse

from . import budget, fitness, grooming, storage


def build_parser():
    p = argparse.ArgumentParser(prog="cowokkit", description="Toolkit harian cowok")
    sub = p.add_subparsers(dest="cmd", required=True)

    e = sub.add_parser("expense", help="catat pengeluaran")
    e.add_argument("amount", type=float)
    e.add_argument("category", choices=budget.CATEGORIES)
    e.add_argument("--note", default="")

    b = sub.add_parser("bmi", help="hitung BMI & kalori harian")
    b.add_argument("weight", type=float)
    b.add_argument("height", type=float)
    b.add_argument("age", type=int)
    b.add_argument("--activity", default="sedang", choices=list(fitness.ACTIVITY))

    w = sub.add_parser("workout", help="catat latihan")
    w.add_argument("name")
    w.add_argument("minutes", type=int)

    g = sub.add_parser("groom", help="tandai/cek perawatan diri")
    g.add_argument("--done", choices=list(grooming.INTERVAL_DAYS))

    sub.add_parser("summary", help="ringkasan pengeluaran")
    return p


def run(argv=None, path=storage.DEFAULT_PATH):
    args = build_parser().parse_args(argv)
    data = storage.load(path)

    if args.cmd == "expense":
        budget.add_expense(data, args.amount, args.category, args.note)
        print(f"Tercatat: Rp{args.amount:,.0f} ({args.category})")
    elif args.cmd == "bmi":
        value = fitness.bmi(args.weight, args.height)
        kcal = fitness.daily_calories(args.weight, args.height, args.age, args.activity)
        print(f"BMI {value} ({fitness.bmi_category(value)}), kebutuhan {kcal} kkal/hari")
    elif args.cmd == "workout":
        fitness.log_workout(data, args.name, args.minutes)
        print(f"Latihan '{args.name}' {args.minutes} menit tercatat")
    elif args.cmd == "groom":
        if args.done:
            grooming.mark_done(data, args.done)
            print(f"{args.done} ditandai selesai")
        else:
            print("Perlu dilakukan:", ", ".join(grooming.overdue_tasks(data)) or "-")
    elif args.cmd == "summary":
        for cat, total in budget.total_by_category(data).items():
            print(f"{cat:<10} Rp{total:,.0f}")

    storage.save(data, path)
    return 0
