<template>
    <div>
        <p>{{ greeting }} {{ obj }}</p>
        <form action="">
            <input type="text" v-model="obj">
        </form>
    </div>
</template>
<script>
module.exports = {
    data: function() {
        return {
            greeting: 'Hello',
            obj: 'World!'
        }
    }
}
</script>
<style>
p {
    font-size: 2em;
    text-align: center;
}
input {
    text-align: center;
    margin-left: 42%;
}
</style>


