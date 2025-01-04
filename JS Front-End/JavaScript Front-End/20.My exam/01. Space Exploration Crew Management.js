function solve(input) {
    let count = input.shift()
    let astronauts = {} 
    
    for (let i = 0; i < count; i++) {
        let [name, section, skills] = input.shift().split(' ')
        skills = skills.split(',')
        astronauts[name] = {section, skills}
    }
    
    let commandLine = input.shift()
    while (commandLine !== 'End') {
        let [command, name, ...args] = commandLine.split(' / ')
        if (command === 'Perform') {
            let section = args[0]
            let skill = args[1]
            if (astronauts[name].section === section && astronauts[name].skills.includes(skill)) {   
                console.log(`${name} has successfully performed the skill: ${skill}!`);
            } else {
                console.log(`${name} cannot perform the skill: ${skill}.`);
            }   
        } else if (command === 'Transfer') {
            let newSection = args[0]
            astronauts[name].section = newSection
            console.log(`${name} has been transferred to: ${newSection}`)
        } else if (command === 'Learn Skill') {
            let newSkill = args[0]
            if (astronauts[name].skills.includes(newSkill)) {
                console.log(`${name} already knows the skill: ${newSkill}.`);
            } else {
                astronauts[name].skills.push(newSkill)
                console.log(`${name} has learned a new skill: ${newSkill}.`);
            }    
        }

        commandLine = input.shift()
    }

    Object.entries(astronauts).forEach(([name, data]) => {
        let sortedSkills = data.skills.sort((a, b) => a.localeCompare(b));
        console.log(
            `Astronaut: ${name}, Section: ${data.section}, Skills: ${sortedSkills.join(', ')}`
        );
    });
}


// {section: 'command_module', skills: 'piloting,communications'}
// {section: 'engineering_bay', skills: 'repair,maintenance'}



solve([ 

    "2", 
  
    "Alice command_module piloting,communications", 
  
    "Bob engineering_bay repair,maintenance", 
  
    "Perform / Alice / command_module / piloting", 
  
    "Perform / Bob / command_module / repair", 
  
    "Learn Skill / Alice / navigation", 
  
    "Perform / Alice / command_module / navigation", 
  
    "Transfer / Bob / command_module", 
  
    "Perform / Bob / command_module / maintenance", 
  
    "End" 
  
  ] )