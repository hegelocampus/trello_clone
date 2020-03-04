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
  display: flex;
  color: white;
  flex-direction: column;
  align-items: center;
  width: 200px;
  height: auto;
  min-height: 400px;
  margin: 5px 10px;
  border-radius: 2rem;
}
</style>
