// gonna use good ol' fs for today
const fs = require('fs');

const rules = Array.from(
        fs.readFileSync('./puzzle-inputs/day7.txt', 'utf8')
        .matchAll(/^\s*(.*) bags contain (.*)\.\s*$/gm)
    )
    .map(parts => ({
        color: parts[1],
        contains: parts[2]
            .split(/,/g)
            .filter(content => !/no other bags/.test(content))
            .map(content => {
                let items = content.match(/^\s*(\d+) (.*) bags?\.?\s*$/);
                return {
                    count: parseInt(items[1]),
                    color: items[2]
                };
            })
    }));

const mapped = rules.reduce((mapped, rule) => {
    mapped.set(rule.color, rule.contains);
    return mapped;
}, new Map());

function canContain(container, target) {
    const rule = mapped.get(container);

    if (!rule) {
        return false;
    }
    else if (rule.some(content => content.color === target)){
        return true;
    }
    else if (rule.some(content => canContain(content.color, target))) {
        return true;
    }
    return false;
}

let setOfBags = new Set(
    rules.filter(rule => canContain(rule.color, 'shiny gold'))
)

console.log(setOfBags.size);

// part 2

function bagsInBag(bag) {
    let content = mapped.get(bag);
    if (!content) {
        return 1;
    }
    let valArr = content.map(thing => 
                                thing.count * (1 + bagsInBag(thing.color)));
    return valArr.reduce((sum, i) => sum + i, 0);
}

console.log(bagsInBag('shiny gold'));