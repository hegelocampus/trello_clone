<template>
  <div class="taskboard">
    <TaskList
      v-for="subTasks in allTasks"
      v-bind:name="subTasks.name"
      v-bind:tasks="subTasks.tasks"
      v-bind:key="subTasks.id"
    />
  </div>
</template>

<script>
import TaskList from "@/components/TaskList.vue";

export default {
  name: "Home",
  components: { TaskList },
  data: () => ({
    name,
    allTasks: [
      { id: 0, name: "To Do", tasks: [{ status: "To Do", text: "test 1" }] },
      { id: 1, name: "Doing", tasks: [] },
      { id: 2, name: "Need Review", tasks: [] },
      { id: 3, name: "Done", tasks: [] }
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
