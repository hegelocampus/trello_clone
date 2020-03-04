<template>
  <div class="task-list">
    <h2>{{ name }}</h2>
    <Task v-for="task in tasks" v-bind:task="task" v-bind:key="task.id" />
  </div>
</template>

<script>
import Task from "@/components/Task.vue";

export default {
  name: "TaskList",
  components: { Task },
  props: ["name", "tasks", "color"]
};
</script>
<style lang="scss">
.task-list {
  width: 200px;
  height: 400px;
}
</style>
