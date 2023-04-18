
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import queue
import threading
from ga.selection_methods.roulette_wheel import RouletteWheel
from ga.selection_methods.tournament import Tournament
from ga.genetic_operators.recombination_one_cut import RecombinationOneCut
from ga.genetic_operators.recombination_two_cuts import RecombinationTwoCuts
from ga.genetic_operators.recombination_uniform import RecombinationUniform
from ga.genetic_operators.mutation_binary import MutationBinary
from ga.genetic_algorithm_thread import GeneticAlgorithmThread
from knapsack.knapsack_problem import build_knapsack
from knapsack.knapsack_problem import KnapsackProblem
from knapsack.knapsack_experiments_factory import KnapsackExperimentsFactory


matplotlib.use("TkAgg")


class Window(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.title('Genetic Algorithms')

        self.protocol('WM_DELETE_WINDOW', self.on_closing)

        self.frame = tk.Frame(master=self)
        self.frame.pack()

        # 0 - OVERALL STRUCTURE ---------------------------------------------

        self.panel_top = tk.PanedWindow(self.frame)
        self.panel_middle = tk.PanedWindow(self.frame)
        self.panel_bottom = tk.PanedWindow(self.frame)
        self.panel_top.pack()
        self.panel_middle.pack()
        self.panel_bottom.pack()

        # 1 - TOP PANEL -----------------------------------------------------

        self.panel_top_left = tk.PanedWindow(self.panel_top)
        self.panel_top_left.pack(side='left')

        self.panel_top_right = tk.PanedWindow(self.panel_top)
        self.panel_top_right.pack(side='left')

        # 1.1 - Top Left Panel

        self.panel_parameters = tk.PanedWindow(self.panel_top_left)
        self.panel_run = tk.PanedWindow(self.panel_top_left)
        self.panel_parameters.pack()
        self.panel_run.pack()

        # 1.1.1 Parameters Panel

        self.label_seed = tk.Label(master=self.panel_parameters, text="Seed: ", anchor="e", width=25)
        self.label_seed.grid(row=0, column=0)

        self.entry_seed = tk.Entry(master=self.panel_parameters, width=17)
        self.entry_seed.insert(tk.END, '1')
        self.entry_seed.grid(row=0, column=1)

        self.label_population_size = tk.Label(master=self.panel_parameters, text="Population size: ",
                                              anchor="e", width=25)
        self.label_population_size.grid(row=1, column=0)

        self.entry_population_size = tk.Entry(master=self.panel_parameters, width=17)
        self.entry_population_size.insert(tk.END, '100')
        self.entry_population_size.grid(row=1, column=1)

        self.label_num_generations = tk.Label(master=self.panel_parameters, text="# of generations: ",
                                              anchor="e", width=25)
        self.label_num_generations.grid(row=2, column=0)

        self.entry_num_generations = tk.Entry(master=self.panel_parameters, width=17)
        self.entry_num_generations.insert(tk.END, '100')
        self.entry_num_generations.grid(row=2, column=1)

        self.label_selection_methods = tk.Label(master=self.panel_parameters, text="Selection method: ",
                                                anchor="e", width=25)
        self.label_selection_methods.grid(row=3, column=0)

        selection_methods = ['Roulette Wheel', 'Tournament']

        self.combo_selection_methods = ttk.Combobox(master=self.panel_parameters, state="readonly",
                                                    values=selection_methods, width=14)
        self.combo_selection_methods.set(selection_methods[0])
        self.combo_selection_methods.grid(row=3, column=1)

        self.label_tournament_size = tk.Label(master=self.panel_parameters, text="Tournament size: ",
                                              anchor="e", width=25)
        self.label_tournament_size.grid(row=4, column=0)

        self.entry_tournament_size = tk.Entry(master=self.panel_parameters, width=17)
        self.entry_tournament_size.insert(tk.END, '2')
        self.entry_tournament_size.grid(row=4, column=1)

        self.label_recombination_methods = tk.Label(master=self.panel_parameters, text="Recombination method: ",
                                                    anchor="e", width=25)
        self.label_recombination_methods.grid(row=5, column=0)

        recombination_methods = ['One cut', 'Two cuts', 'Uniform']

        self.combo_recombination_methods = ttk.Combobox(master=self.panel_parameters, state="readonly",
                                                        values=recombination_methods, width=14)
        self.combo_recombination_methods.set(recombination_methods[0])
        self.combo_recombination_methods.grid(row=5, column=1)

        self.label_recombination_prob = tk.Label(master=self.panel_parameters, text="Recombination prob.: ",
                                                 anchor="e", width=25)
        self.label_recombination_prob.grid(row=6, column=0)

        self.entry_recombination_prob = tk.Entry(master=self.panel_parameters, width=17)
        self.entry_recombination_prob.insert(tk.END, '0.7')
        self.entry_recombination_prob.grid(row=6, column=1)

        self.label_mutation_prob = tk.Label(master=self.panel_parameters, text="Mutation prob.: ", anchor="e", width=25)
        self.label_mutation_prob.grid(row=7, column=0)

        self.entry_mutation_prob = tk.Entry(master=self.panel_parameters, width=17)
        self.entry_mutation_prob.insert(tk.END, '0.01')
        self.entry_mutation_prob.grid(row=7, column=1)

        self.label_prob1s = tk.Label(master=self.panel_parameters, text="Initial proportion of 1s: ",
                                     anchor="e", width=25)
        self.label_prob1s.grid(row=8, column=0)

        self.entry_prob1s = tk.Entry(master=self.panel_parameters, width=17)
        self.entry_prob1s.insert(tk.END, '0.05')
        self.entry_prob1s.grid(row=8, column=1)

        self.label_fitness_type = tk.Label(master=self.panel_parameters, text="Fitness type: ",
                                           anchor="e", width=25)
        self.label_fitness_type.grid(row=9, column=0)

        fitness_types = ['Simple', 'With penalty']

        self.combo_fitness_type = ttk.Combobox(master=self.panel_parameters, state="readonly",
                                               values=fitness_types, width=14)
        self.combo_fitness_type.set(fitness_types[0])
        self.combo_fitness_type.grid(row=9, column=1)

        # 1.1.2 Run Panel

        self.button_dataset = tk.Button(master=self.panel_run, text='Problem',
                                        command=self.problem_button_clicked)
        self.button_dataset.pack(side='left', padx=5)

        self.button_run = tk.Button(master=self.panel_run, text='Run',
                                    command=self.run_button_clicked)
        self.button_run.pack(side='left', padx=5)

        self.button_stop = tk.Button(master=self.panel_run, text='Stop',
                                     command=self.stop_button_clicked)
        self.button_stop.pack(side='left', padx=5)

        # 1.2 Top Right Panel

        # Nothing to be done here

        # 2 - MIDDLE PANEL --------------------------------------------------

        self.panel_problem = tk.PanedWindow(self.panel_middle)
        self.panel_problem.pack(side='left', padx=5)

        self.panel_best = tk.PanedWindow(self.panel_middle)
        self.panel_best.pack(side='left', padx=5)

        # 2.1 ProblemPanel

        self.label_problem = tk.Label(master=self.panel_problem, text="Problem data: ", anchor="w", width=46)
        self.label_problem.pack()
        self.text_problem = tk.Text(master=self.panel_problem, state="normal", height=20, width=40)
        self.text_problem.pack()

        # 2.2 Best Panel

        self.label_best = tk.Label(master=self.panel_best, text="Best solution: ", anchor="w", width=46)
        self.label_best.pack()
        self.text_best = tk.Text(master=self.panel_best, state="normal", height=20, width=40)
        self.text_best.pack()

        # 3 - BOTTOM PANEL --------------------------------------------------

        self.button_experiments = tk.Button(master=self.panel_bottom, text='Open experiments',
                                            command=self.open_experiments_button_clicked)
        self.button_experiments.pack(side='left', padx=5)

        self.button_run_experiments = tk.Button(master=self.panel_bottom, text='Run',
                                                command=self.run_experiments_button_clicked)
        self.button_run_experiments.pack(side='left', padx=5)

        self.button_stop_experiments = tk.Button(master=self.panel_bottom, text='Stop',
                                                 command=self.stop_experiments_button_clicked)
        self.button_stop_experiments.pack(side='left', padx=5)

        self.label_status = tk.Label(master=self.panel_bottom, text="status: ")
        self.label_status.pack(side="left", padx=5)

        self.entry_status = tk.Entry(master=self.panel_bottom, width=10)
        self.entry_status.pack(side="left", padx=3)

        # -----------------------------------------------------

        self.knapsack_problem = None
        self.genetic_algorithm = None

        self.generations = None
        self.generation_values = None
        self.average_values = None
        self.best_values = None
        self.line_average_values = None
        self.line_best_values = None
        self.canvas_plot = None
        self.ax = None
        self.after_id = None
        self.queue = queue.Queue()

        self.draw_empty_plot()

        self.experiments_factory = None
        self.experiments_runner = None

        # End of constructor -----------------------------------

    def problem_button_clicked(self):
        filename = fd.askopenfilename(initialdir='.')
        if filename:
            self.knapsack_problem = build_knapsack(filename)
            self.text_problem .delete("1.0", "end")
            self.text_problem.insert(tk.END, str(self.knapsack_problem))
            self.manage_buttons(data_set=tk.NORMAL, run=tk.NORMAL, stop=tk.DISABLED,
                                open_experiments=tk.NORMAL, run_experiments=tk.DISABLED, stop_experiments=tk.DISABLED)
            self.entry_status.delete(0, tk.END)

    def run_button_clicked(self):

        if self.knapsack_problem is None:
            messagebox.showwarning("Warning", "You should define a problem first (Problem button)")
            return

        if not self.validate_parameters():
            return

        selection_method = \
            RouletteWheel() if self.combo_selection_methods.current() == 0 else \
            Tournament(int(self.entry_tournament_size.get()))
        recombination_methods_index = self.combo_recombination_methods.current()
        recombination_method = \
            RecombinationOneCut(float(self.entry_recombination_prob.get())) if recombination_methods_index == 0 else \
            RecombinationTwoCuts(float(self.entry_recombination_prob.get())) if recombination_methods_index == 1 else \
            RecombinationUniform(float(self.entry_recombination_prob.get()))
        mutation_method = MutationBinary(float(self.entry_mutation_prob.get()))
        self.knapsack_problem.prob1s = float(self.entry_prob1s.get())
        self.knapsack_problem.fitness_type = \
            KnapsackProblem.SIMPLE_FITNESS if self.combo_fitness_type.current() == 0 else \
            KnapsackProblem.PENALTY_FITNESS

        self.genetic_algorithm = GeneticAlgorithmThread(
            int(self.entry_seed.get()),
            int(self.entry_population_size.get()),
            int(self.entry_num_generations.get()),
            selection_method,
            recombination_method,
            mutation_method
        )

        self.queue.queue.clear()
        self.generations = 0
        self.generation_values = []
        self.average_values = []
        self.best_values = []

        self.genetic_algorithm.problem = self.knapsack_problem
        self.genetic_algorithm.add_tkinter_listener(self)
        self.genetic_algorithm.daemon = True
        self.genetic_algorithm.start()
        self.update_idletasks()
        self.after_id = self.after(0, self.generation_ended)
        self.manage_buttons(data_set=tk.DISABLED, run=tk.DISABLED,  stop=tk.NORMAL,
                            open_experiments=tk.DISABLED, run_experiments=tk.DISABLED, stop_experiments=tk.DISABLED)
        self.entry_status.delete(0, tk.END)

    def stop_button_clicked(self):
        if self.genetic_algorithm is not None:
            self.genetic_algorithm.stop()
        self.manage_buttons(data_set=tk.NORMAL, run=tk.NORMAL,  stop=tk.DISABLED,
                            open_experiments=tk.NORMAL, run_experiments=tk.DISABLED, stop_experiments=tk.DISABLED)
        self.queue.queue.clear()
        self.after_cancel(self.after_id)

    def open_experiments_button_clicked(self):
        filename = fd.askopenfilename(initialdir='.')
        if filename:
            self.experiments_factory = KnapsackExperimentsFactory(filename)
            self.manage_buttons(data_set=self.button_dataset['state'], run=self.button_run['state'],  stop=tk.DISABLED,
                                open_experiments=tk.NORMAL, run_experiments=tk.NORMAL, stop_experiments=tk.DISABLED)

    def run_experiments_button_clicked(self):
        self.experiments_runner = ExperimentsRunner(self)
        self.experiments_runner.daemon = True
        self.experiments_runner.start()
        self.manage_buttons(data_set=tk.DISABLED, run=tk.DISABLED,  stop=tk.DISABLED,
                            open_experiments=tk.DISABLED, run_experiments=tk.DISABLED, stop_experiments=tk.NORMAL)
        self.entry_status.delete(0, tk.END)
        self.entry_status.insert(tk.END, 'Running')

    def stop_experiments_button_clicked(self):
        if self.experiments_runner is not None:
            self.experiments_runner.stop()
        self.manage_buttons(data_set=tk.NORMAL, run=tk.DISABLED, stop=tk.DISABLED,
                            open_experiments=tk.NORMAL, run_experiments=tk.NORMAL, stop_experiments=tk.DISABLED)

    def on_closing(self):
        if self.genetic_algorithm:
            self.genetic_algorithm.stop()
        if self.experiments_runner:
            self.experiments_runner.stop()
        self.destroy()

    def manage_buttons(self, data_set, run, stop, open_experiments, run_experiments, stop_experiments):
        self.button_dataset['state'] = data_set
        self.button_run['state'] = run
        self.button_stop['state'] = stop
        self.button_experiments['state'] = open_experiments
        self.button_run_experiments['state'] = run_experiments
        self.button_stop_experiments['state'] = stop_experiments

    def generation_ended(self):
        if not self.queue.empty():
            ga_info = self.queue.get()
            if ga_info.run_ended:
                self.queue.queue.clear()
                self.after_cancel(self.after_id)
                self.manage_buttons(data_set=tk.NORMAL, run=tk.NORMAL, stop=tk.DISABLED,
                                    open_experiments=tk.NORMAL, run_experiments=tk.DISABLED,
                                    stop_experiments=tk.DISABLED)
                return
            self.text_best.delete("1.0", "end")
            self.text_best.insert(tk.END, str(ga_info.best))
            self.generation_values.append(self.generations)
            self.average_values.append(ga_info.average_fitness)
            self.best_values.append(ga_info.best.fitness)
            self.generations += 1
            self.update_plot()
        self.update_idletasks()
        self.after_id = self.after(0, self.generation_ended)

    def draw_empty_plot(self):
        fig = Figure(figsize=(5, 2.5), dpi=100)
        self.ax = fig.add_subplot(111)
        self.line_average_values, = self.ax.plot([], [], label='Average')
        self.line_best_values, = self.ax.plot([], [], label='Best')
        self.ax.legend()
        self.canvas_plot = FigureCanvasTkAgg(fig, master=self.panel_top_right)
        self.canvas_plot.draw()
        self.canvas_plot.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)

    def update_plot(self):
        self.line_average_values.set_data(self.generation_values, self.average_values)
        self.line_best_values.set_data(self.generation_values, self.best_values)
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas_plot.draw()

    def validate_parameters(self) -> bool:
        try:
            seed = int(self.entry_seed.get())
            if seed <= 0:
                messagebox.showwarning("Warning", "Seed should be a positive integer")
                return False
        except ValueError:
            messagebox.showwarning("Warning", "Seed should be a positive integer")
            return False

        try:
            population_size = int(self.entry_population_size.get())
            if population_size <= 1 or population_size % 2 != 0:
                messagebox.showwarning("Warning", "Population size should be an even positive integer")
                return False
        except ValueError:
            messagebox.showwarning("Warning", "Population size should be an even positive integer")
            return False

        try:
            num_generations = int(self.entry_num_generations.get())
            if num_generations <= 0:
                messagebox.showwarning("Warning", "Number of generations should be a positive integer")
                return False
        except ValueError:
            messagebox.showwarning("Warning", "Number of generations should be a positive integer")
            return False

        if self.combo_selection_methods.current() == 1:
            try:
                tournament_size = int(self.entry_tournament_size.get())
                if tournament_size < 2 or tournament_size > population_size - 1:
                    messagebox.showwarning("Warning", "Tournament size should be a positive integer larger than 1"
                                                      " and smaller than the population size")
                    return False
            except ValueError:
                messagebox.showwarning("Warning", "Tournament size should be a positive integer larger than 1"
                                                  " and smaller than the population size")
                return False

        try:
            recombination_prob = float(self.entry_recombination_prob.get())
            if recombination_prob < 0 or recombination_prob > 1:
                messagebox.showwarning("Warning", "Recombination probability should be a float in [0, 1]")
                return False
        except ValueError:
            messagebox.showwarning("Warning", "Recombination probability should be a float in [0, 1]")
            return False

        try:
            mutation_prob = float(self.entry_mutation_prob.get())
            if mutation_prob < 0 or mutation_prob > 1:
                messagebox.showwarning("Warning", "Mutation probability should be a float in [0, 1]")
                return False
        except ValueError:
            messagebox.showwarning("Warning", "Mutation probability should be a float in [0, 1]")
            return False

        try:
            prob1s = float(self.entry_prob1s.get())
            if prob1s < 0 or prob1s > 1:
                messagebox.showwarning("Warning", "The probability of a gene being 1 should be a float in [0, 1]")
                return False
        except ValueError:
            messagebox.showwarning("Warning", "The probability of a gene being 1 should be a float in [0, 1]")
            return False

        if self.combo_selection_methods.current() == 0 and self.combo_fitness_type.current() == 1:
            messagebox.showwarning("Warning", "Roulette wheel should not be used with Penalty fitness")
            return False

        return True


class ExperimentsRunner(threading.Thread):

    def __init__(self, gui: Window):
        super(ExperimentsRunner, self).__init__()
        self.gui = gui
        self.experiments_factory = gui.experiments_factory
        self.thread_running = False

    def stop(self):
        self.thread_running = False

    def run(self):
        self.thread_running = True
        while self.experiments_factory.has_more_experiments() and self.thread_running:
            experiment = self.experiments_factory.next_experiment()
            experiment.run()

        self.gui.text_best.insert(tk.END, '')
        if self.thread_running:
            self.gui.entry_status.delete(0, tk.END)
            self.gui.entry_status.insert(tk.END, 'Done')
            self.gui.manage_buttons(data_set=tk.NORMAL, run=tk.DISABLED, stop=tk.DISABLED,
                                    open_experiments=tk.NORMAL, run_experiments=tk.DISABLED,
                                    stop_experiments=tk.DISABLED)

