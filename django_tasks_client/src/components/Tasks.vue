<template>
  <div class="tasks_container">
    <div class="tasks_content">
        <h1>Tasks</h1>
        <ul class="tasks_list">
            <li v-for="task in tasks" :key="task.id" class="task">
                <h2>{{ task.title }}</h2>
                <p>{{ task.description }}</p>
                <p>{{ task.completed }}</p>
                <span>
                    <button @click="saveTask(task)">Modify</button>
                    <button @click="deleteTask(task)">Delete</button>
                </span>
            </li>
        </ul>
    </div>

    <div class="style_task" v-if="!update_task">
        <form v-on:submit.prevent="createTask">
            <h3>Create task</h3>
            <div class="form-group">
                <label for="title">Title</label>
                <input type="text" v-model="title">
            </div>
            <div class="form-group">
                <label for="description">Description</label>
                <textarea v-model="description"></textarea>
            </div>
            <div class="form-group">
                <button type="submit">Add Task</button>
            </div>
        </form>
    </div>

    <div class="style_task" v-if="update_task">
        <form v-on:submit.prevent="modifyTask(update_task)">
            <h3>Modify task</h3>
            <div class="form-group">
                <label for="title">Title</label>
                <input type="text" v-model="update_task.title">
            </div>
            <div class="form-group">
                <label for="description">Description</label>
                <textarea v-model="update_task.description"></textarea>
            </div>
            <div class="form-group">
                <label for="completed">Completed</label>
                <input type="checkbox" v-model="update_task.completed">
            </div>
            <div class="form-group">
                <button type="submit">Modify Task</button>
            </div>
        </form>
    </div>

  </div>
</template>

<script>
export default {
    name: 'TasksComponent',
    data() {
        return {
            // tasks
            tasks: [''],
            new_task: null,
            update_task: null,
            title: '',
            description: '',
            completed: false,
        }
    },
    created() {
        // console.log("component created")
        this.getData();
    },
    methods: {
        saveTask(task) {
            this.update_task = task
        },
        async getData() {
            try {
                await this.$http
                .get('http://localhost:8000/task/')
                .then((response) => {
                    this.tasks = response.data;
                });
            } catch (error) {
                console.log(error);
            }
        },
        async createTask() {
            console.log("inside create task function")
            try {
                await this.$http
                .post('http://localhost:8000/task/', {
                    title: this.title,
                    description: this.description,
                    completed: false
                })
                .then((response) => {
                    console.log("response.data: ", response.data)
                    this.tasks.push(response.data)
                    this.title = ''
                    this.description = ''
                    this.completed = false
                });
            } catch (error) {
                console.log(error);
            }
        },
        async modifyTask(payload){
            const task = payload
            try {
                console.log("inside update task function")
                await this.$http
                .put('http://localhost:8000/task/' + task.id + '/', {
                    title: task.title,
                    description: task.description,
                    completed: task.completed,
                })
                .then((response) => {
                    console.log(response);

                    this.title = ''
                    this.description = ''
                    this.completed = false
                    this.update_task = null
                    this.getData()
                });
            } catch (error) {
                console.log(error);
            }
        },
        async deleteTask(task){
            console.log("inside delete task function")
            try{
                await this.$http.delete('http://localhost:8000/task/' + task.id + '/')
                this.getData()
            }
            catch(err){
                console.log(err)
            }
        },

        
    },
}
</script>

<style>
    .tasks_aontainer{
        width: 100%;
    }
    .tasks_content h1{
        color: rgb(243, 79, 142);
        /* border-bottom: 1px solid red; */
        width: 30%;
        margin: 20px auto;
        font-size: 40px;
    }
    .tasks_list{
        width: 95%;
        padding: 20px;
        margin: auto;
        list-style: none;
        display: grid; 
        grid-template-columns: 1fr 1fr; 
        grid-auto-rows: 1fr;
        grid-column-gap: 20px; 
        /* grid-row-gap: 30px; */
        border: 1px solid rgb(243, 79, 142); 
        background: rgb(174, 240, 252, 0.5);

        /* width: 50%;  */
    }
    .tasks_list h2{
        color: rgb(66, 85, 250);
        margin: 30px;
        font-size: 20px;
    }
    .tasks_list li{
        /* border: 1px solid red; */
        text-align: center;
    }
    .task{
        text-align: center;
        /* border-bottom: 1px solid rgb(243, 79, 142); */
        padding: 10px;
        background: rgba(255, 255, 255, 0.6);
        margin: 10px;
    }
    button{
        border: none;
        margin: auto 10px;
        background: none;
        background: rgb(252, 179, 207);
        padding: 10px;
        /* color: white; */
    }
    button:active{
        background: rgb(243, 79, 142);
    }
    .style_task{
        width: 95%;
        border: 1px solid rgb(243, 79, 142); 
        background: rgb(174, 240, 252, 0.5);
        margin: 20px auto;
        padding: 20px;
    }
    .style_task h3{
        font-size: 25px;
        color: rgb(66, 85, 250);
    }
    .form-group{
        text-align: center;
    }
    .form-group label{
        display: block;
        padding: 10px 0;
        text-align: center;
    }
    .form-group input, textarea{
        width: 50%;
        padding: 10px 0;
        margin: 10px; 
        padding: 5px;
    }
    .form-group button{
        width: 30%;
        padding: 10px 0;
        margin: 10px; 
    }
</style>