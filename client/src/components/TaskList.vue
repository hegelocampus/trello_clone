<template>
  <div class="task-list">
    <h2>{{ name }}</h2>
    <draggable
      v-model="tasks"
      :group="{ name: 'tasks' }"
      @start="drag = true"
      @end="drag = false"
    >
      <Task v-for="task in tasks" :task="task" :key="task.id" />
    </draggable>
  </div>
</template>

<script>
import Task from "@/components/Task.vue";
import draggable from "vuedraggable";

export default {
  name: "TaskList",
  components: { Task, draggable },
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
