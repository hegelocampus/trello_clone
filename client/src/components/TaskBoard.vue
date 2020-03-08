<template>
  <div class="taskboard">
    <TaskList
      v-for="(subTasks, idx) in allTasks"
      :key="idx"
      v-bind:name="subTasks.name"
      v-bind:tasks="subTasks.tasks"
      v-bind:style="{ backgroundColor: subTasks.color }"
    />
  </div>
</template>

<script>
import TaskList from "@/components/TaskList.vue";
//import store from "../../store/index.js";

// TODO: Retreive this data using an AJAX request
const todoTasks = [
  { status: "To Do", text: "test 1" },
  { status: "To Do", text: "test 2" }
];
const doingTasks = [];
const reviewTasks = [];
const doneTasks = [];

export default {
  name: "Home",
  components: { TaskList },
  data: () => ({
    name,
    allTasks: [
      { name: "To Do", color: "#007979", tasks: todoTasks },
      { name: "Doing", color: "#c60127", tasks: doingTasks },
      { name: "Review", color: "#fdd200", tasks: reviewTasks },
      { name: "Done", color: "#2f3879", tasks: doneTasks }
    ]
  }),
  methods: {
    onEnd: ({ target }) => {
      // Invoke Vuex dispatch
      console.log(target);
      return target;
    }
  }
};
</script>

<style lang="scss">
.taskboard {
  display: flex;
  box-sizing: border-box;
  height: 100%;
  width: 95%;
  background-color: #c0fcff;
  border-radius: 2rem;
  padding: 10px 15px 10px 15px;
  margin: 10px 20px 10px 20px;
}
</style>
