#ifndef GUARD_grammer_h
#define GUARD_grammer_h

#include <vector>
#include <map>

typedef std::vector<std::string> Rule;
typedef std::vector<Rule> Rule_collection;
typedef std::map<std::string, Rule_collection> Grammer;

std::vector<std::string> gen_sentence(const Grammer&);
bool bracketed(const std::string&);
void gen_aux(const Grammer&, const std::string&, std::vector<std::string>&);

#endif
