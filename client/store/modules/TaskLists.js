// Use hashmap to store task status and index
const state = {
  taskStatus: {},
  allTasks: [
    { name: "To Do", color: "#007979", tasks: [] },
    { name: "Doing", color: "#c60127", tasks: [] },
    { name: "Review", color: "#fdd200", tasks: [] },
    { name: "Done", color: "#2f3879", tasks: [] }
  ]
};

const getters = {};

const actions = {};

const mutations = {
  updateTasks(state, tasks) {
    const parsedTasks = tasks.reduce(
      (acc, task) => {
        switch (task.name) {
          case "To Do":
            acc[0].push(task);
            break;
          case "Doing":
            acc[1].push(task);
            break;
          case "Review":
            acc[2].push(task);
            break;
          case "Done":
            acc[3].push(task);
            break;
        }
      },
      [[], [], [], []]
    );

    // Construct new state
    state = {
      allTasks: parsedTasks
    };
  },
  updateTaskStatus(state /*task, newStatus*/) {
    return state;
  }
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
};
