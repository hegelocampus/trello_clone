
// Use hashmap to store task status and index
const state = {
  taskStatus: {
  },
  allTasks: {
    "To Do": { color: "#007979", tasks: [] },
    "Doing": { color: "#c60127", tasks: [] },
    "Review": { color: "#fdd200", tasks: [] },
    "Done": { color: "#2f3879", tasks: [] }
  }
};

const getters = {
};

const actions = {
};

const mutations = {
  updateTaskStatus: (state, task, newStatus) => {
    state
  }
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}

