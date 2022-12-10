import java.io.InputStream;
import java.util.Iterator;
import java.util.Scanner;

public class Day10 {
    class Machine {
        enum Opcode {
            NOOP(1),
            ADDX(2);

            private final int cycles;

            Opcode(int cycles) {
                this.cycles = cycles;
            }
        }
        record Instruction(Opcode opcode, int arg) {};

        public static final int CRT_WIDTH = 40;
        private Iterator<Instruction> ops;
        private boolean end;

        private int X = 1, cycle = 0, opCyclesRemaining = 0, sample = 0;
        private Instruction currOp;
        private StringBuffer crt;

        Machine(Iterator<Instruction> ops) {
            this.ops = ops;
            this.crt = new StringBuffer();
        }

        public void step() {
            instructionFetch();
            if (!end) {
                sample = X * cycle;
                updateCrt();
                execute();
            }
        }

        public int sampleAt(int cycle) {
            while (!end && this.cycle != cycle) {
                step();
            }
            return sample;
        }

        public void run() {
            sampleAt(Integer.MAX_VALUE);
        }

        private void instructionFetch() {
            cycle++;
            if (opCyclesRemaining == 0) {
                if (!ops.hasNext()) {
                    end = true;
                    return;
                }

                currOp = ops.next();
                opCyclesRemaining = currOp.opcode.cycles;
            }
        }

        private void execute() {
            opCyclesRemaining--;
            if (opCyclesRemaining == 0) {
                X += switch (currOp.opcode) {
                    case NOOP -> 0;
                    case ADDX -> currOp.arg;
                };
            }
        }

        private void updateCrt() {
            int crtX = (cycle - 1) % CRT_WIDTH;
            crt.append(crtX - 1 <= X && X <= crtX + 1 ? '#' : '.');
        }

        public StringBuffer getCrt() {
            return crt;
        }
    }

    private static final int[] SAMPLE_POINTS = new int[]{20, 60, 100, 140, 180, 220};

    void start() {
        int sampleSum = 0;
        Machine machine = new Machine(getInstructions(System.in));
        for (int samplePoint: SAMPLE_POINTS) {
            sampleSum += machine.sampleAt(samplePoint);
        }
        machine.run();

        System.out.println(sampleSum);
        printCrt(machine);
    }

    void printCrt(Machine machine) {
        StringBuffer crt = machine.getCrt();
        for (int i = 0; i < crt.length(); i += Machine.CRT_WIDTH) {
            String line = crt.substring(i, Math.min(i + Machine.CRT_WIDTH, crt.length()));
            System.out.println(line);
        }
    }

    Iterator<Machine.Instruction> getInstructions(InputStream input) {
        return new Iterator<>() {
            Scanner in = new Scanner(input);

            @Override
            public boolean hasNext() {
                return in.hasNext();
            }

            @Override
            public Machine.Instruction next() {
                if (in.next().equals("noop")) {
                    return new Machine.Instruction(Machine.Opcode.NOOP, 0);
                }

                return new Machine.Instruction(Machine.Opcode.ADDX, in.nextInt());
            }
        };
    }

    public static void main(String[] args) {
        new Day10().start();
    }
}