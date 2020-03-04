<template>
  <div class="taskboard">
    <TaskList
      v-for="subTasks in allTasks"
      v-bind:name="subTasks.name"
      v-bind:tasks="subTasks.tasks"
      v-bind:key="subTasks.id"
      v-bind:style="{ backgroundColor: subTasks.color }"
    />
  </div>
</template>

<script>
import TaskList from "@/components/TaskList.vue";

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
      { id: 0, name: "To Do", color: "#007979", tasks: todoTasks },
      { id: 1, name: "Doing", color: "#c60127", tasks: doingTasks },
      { id: 2, name: "Need Review", color: "#fdd200", tasks: reviewTasks },
      { id: 3, name: "Done", color: "#2f3879", tasks: doneTasks }
    ]
  })
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
  margin: 10px 20px 10px 20px;
}
</style>
